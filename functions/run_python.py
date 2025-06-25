import os
import subprocess
import sys

def run_python_file(working_directory, file_path):
    try:
        wd = os.path.abspath(working_directory)
        target = os.path.abspath(os.path.join(working_directory, file_path))

        if os.path.commonpath([wd, target]) != wd:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(target):
            return f'Error: File "{file_path}" not found.'

        if not target.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        try:
            proc = subprocess.run(
                [sys.executable, file_path],
                cwd=working_directory,
                capture_output=True,
                text=True,
                timeout=30,
            )
        except subprocess.TimeoutExpired as e:
            out = e.stdout or ""
            err = e.stderr or ""
            return f"STDOUT:{out}STDERR:{err}Process exited with code -1 (timeout)"

        output = ""
        if proc.stdout:
            output += f"STDOUT:{proc.stdout}"
        if proc.stderr:
            output += f"STDERR:{proc.stderr}"
        if proc.returncode != 0:
            output += f"Process exited with code {proc.returncode}"
        if not output:
            output = "No output produced."
        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"
