from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads file content up to 10000 chars",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Directory path to get file content",
            ),
        },
    )
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Actual file path"
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Directory path to run pyhton file",
            ),
        },
        required=["file_path"]
    )
)


schema_write_file= types.FunctionDeclaration(
    name="write_file",
    description="Run python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Actual file path"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content string that wants to be written"

            )
        },
    )
)


available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_get_file_content, schema_run_python_file, schema_write_file],
)
