
import os

def write_file(working_directory:str, file_path:str, content):

    try:
        working_dir_abs = os.path.abspath(working_directory)

        joined_path = os.path.join(working_dir_abs,file_path)

        normal_path = os.path.normpath(joined_path)

        dir_path = os.path.dirname(normal_path)


        valid_path = os.path.commonpath([working_dir_abs,joined_path]) == working_dir_abs

        is_dir = os.path.isdir(normal_path)

        if not valid_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        if is_dir:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(dir_path, exist_ok=True)

        with open(normal_path, "w") as f:
            f.write(content)

            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error reading content: {e}"
