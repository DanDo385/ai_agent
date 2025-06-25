import os

def write_file(working_directory, file_path, content):
    try:
        # Get absolute, normalized paths
        wd = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, file_path))

        # Ensure target is within working_directory
        if os.path.commonpath([wd, target]) != wd:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Make sure directory exists
        parent = os.path.dirname(target)
        if parent and not os.path.exists(parent):
            os.makedirs(parent, exist_ok=True)

        # Write/overwrite the file
        with open(target, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
