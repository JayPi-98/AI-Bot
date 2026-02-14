
import os

MAX_CHARS = 10000

def get_file_content(working_directory , file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)

        joined_path = os.path.join(working_dir_abs,file_path)

        normal_path = os.path.normpath(joined_path)


        valid_path = os.path.commonpath([working_dir_abs,joined_path]) == working_dir_abs

        is_file = os.path.isfile(normal_path)

        if not valid_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not is_file:
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(normal_path, "r") as f:
            files_content_string = f.read(MAX_CHARS)

            # After reading the first MAX_CHARS...
            if f.read(1):
                files_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return files_content_string
    except Exception as e:
        return f"Error reading content: {e}"