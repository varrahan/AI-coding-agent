import os
from google.genai import types
from google.genai.types import FunctionDeclaration, Schema

def write_file(working_dir: str, file_path: str, content: str) -> str:
    abs_working_dir: str = os.path.abspath(working_dir)
    abs_file_path: str = os.path.abspath(os.path.join(working_dir, file_path))


    if (not abs_file_path.startswith(abs_working_dir)):
        return f'Error: Cannot read "{file_path}" as it is outside working directory'
    
    try:
        with open(abs_file_path, "w") as file:
            file.write(content)
    
    except Exception as ex:
        return f"Exception has occured in the write_file function: {ex}"
    
    return f"{file_path} has been written into"

schema_write_file = FunctionDeclaration(
    name="write_file",
    description="Overwrites an existing file or writes to a new file if it does not exist. Creates required parent directories safely",
    parameters=Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": Schema(
                type=types.Type.STRING,
                description="The path to the file that will be read, from the working directory.",
            ),
            "content": Schema(
                type=types.Type.STRING,
                description="The contents that will be written into the file.",
            ),           
        },
    ),
)