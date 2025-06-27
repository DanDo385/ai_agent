import os

def get_files_info(working_directory, directory=None):
    try:
        # Build the absolute path of the directory to inspect
        target_dir = directory or "."
        abs_working = os.path.abspath(working_directory)
        abs_target = os.path.abspath(os.path.join(working_directory, target_dir))

        # Security check: Must be inside the working directory
        if not abs_target.startswith(abs_working):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_target):
            return f'Error: "{directory}" is not a directory'

        entries = []
        for entry in os.listdir(abs_target):
            full_path = os.path.join(abs_target, entry)
            is_dir = os.path.isdir(full_path)
            try:
                size = os.path.getsize(full_path)
            except Exception:
                size = "unknown"
            entries.append(f'- {entry}: file_size={size} bytes, is_dir={is_dir}')

        # Join results or note empty dir
        return "\n".join(entries) if entries else "(empty directory)"
    except Exception as e:
        return f"Error: {e}"
