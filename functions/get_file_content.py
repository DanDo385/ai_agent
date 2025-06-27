import os

def get_file_content(working_directory, file_path):
    try:
        abs_working = os.path.abspath(working_directory)
        abs_file = os.path.abspath(os.path.join(working_directory, file_path))

        if not abs_file.startswith(abs_working):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abs_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        MAX_CHARS = 10000
        with open(abs_file, "r") as f:
            content = f.read(MAX_CHARS)
            rest = f.read(1)
        if rest:
            content += f'\n[...File "{file_path}" truncated at 10000 characters]'
        return content
    except Exception as e:
        return f"Error: {e}"
