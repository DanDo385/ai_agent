import os

def write_file(working_directory, file_path, content):
    try:
        # Normalize paths
        wd = os.path.abspath(working_directory)
        target = os.path.abspath(file_path)

        # Check within working_directory
        common = os.path.commonpath([wd, target])
        if common != wd:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Create directories if needed
        dir_name = os.path.dirname(target)
        if dir_name and not os.path.exists(dir_name):
            os.makedirs(dir_name, exist_ok=True)

        # Write
        with open(target, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
