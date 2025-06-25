import os
import sys
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Check for a prompt argument
if len(sys.argv) < 2:
    print("Error: Please provide a prompt as a command line argument.")
    sys.exit(1)

# Handle prompt and --verbose flag
prompt = sys.argv[1]
verbose = False

# If there's a third argument and it's --verbose
if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
    verbose = True

# Create Gemini client
client = genai.Client(api_key=api_key)

# Generate response
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=prompt
)

# Always print the model's response
print(response.text)

# Print additional info if --verbose
if verbose:
    print(f'User prompt: {prompt}')
    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
