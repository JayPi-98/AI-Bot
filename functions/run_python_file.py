import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        absolute_file_path = os.path.abspath(os.path.join(working_dir_abs, file_path))

        valid_path = os.path.commonpath([working_dir_abs, absolute_file_path]) == working_dir_abs
        if not valid_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        _, ext = os.path.splitext(absolute_file_path)
        if ext.lower() != ".py":
            return f'Error: "{file_path}" is not a Python file'

        command = [sys.executable, absolute_file_path]
        if args is not None:
            command.extend(args)

        cp = subprocess.run(command, cwd=working_dir_abs, text=True, timeout=30, capture_output=True)

        output = []
        if cp.returncode != 0:
            output.append(f"Process exited with code {cp.returncode}")

        if not cp.stdout and not cp.stderr:
            output.append("No output produced")
        else:
            if cp.stdout:
                output.append(f"STDOUT: {cp.stdout}")
            if cp.stderr:
                output.append(f"STDERR: {cp.stderr}")

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
