import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
from functions.write_file import write_file

def call_function(function_call_part, verbose=False):
    function_name = function_call_part.name
    args = dict(function_call_part.args) if hasattr(function_call_part.args, 'items') else function_call_part.args

    # Always add working_directory, since the LLM will never provide it.
    args["working_directory"] = "./calculator"

    # Function name -> actual function mapping
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    if verbose:
        print(f"Calling function: {function_name}({args})")
    else:
        print(f" - Calling function: {function_name}")

    func = function_map.get(function_name)
    if not func:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    try:
        function_result = func(**args)
    except Exception as e:
        function_result = f"Function raised an error: {e}"

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )

# 1. Load environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# 2. System prompt for LLM agent
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

# 3. Define function schemas
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the contents of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read, relative to the working directory.",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file with optional arguments, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The Python file to execute, relative to the working directory.",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites a file with the given content, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)

# 4. Register all schemas as available tools
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

model_name = "gemini-2.0-flash-001"

# 5. Get user prompt from CLI (handle --verbose)
verbose = False
cli_args = sys.argv[1:]
if "--verbose" in cli_args:
    verbose = True
    cli_args.remove("--verbose")

if len(cli_args) > 0:
    messages = " ".join(cli_args)
else:
    print("Please provide a prompt.")
    sys.exit(1)

# 6. Call Gemini with function tools
response = client.models.generate_content(
    model=model_name,
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
    ),
)

# 7. Print function call if present, else print response text
if response.function_calls:
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose=verbose)
        if (
            not hasattr(function_call_result.parts[0], "function_response")
            or not hasattr(function_call_result.parts[0].function_response, "response")
        ):
            raise RuntimeError("Fatal: Function did not return expected response format.")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
else:
    print(response.text)
