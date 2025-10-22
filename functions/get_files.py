import os
from google.genai import types
from google.genai.types import FunctionDeclaration, Schema


def get_files_info(working_dir: str, dir: str = ".") -> str:
    abs_working_dir: str = os.path.abspath(working_dir)
    abs_dir: str = os.path.abspath(os.path.join(working_dir, dir))
    
    if (not abs_dir.startswith(abs_working_dir)):
        return f'Error: "{dir}" is outside of the working directory'
    
    if (not os.path.isdir(abs_dir)):
        return f'Error: "{dir}" is not a directory'
    contents: list[str] = os.listdir(abs_dir)
    
    result: str = ""
    
    for content in contents:
        path: str = os.path.join(abs_dir, content)
        is_dir: bool = os.path.isdir(path)
        file_size: int = os.path.getsize(path)
        
        result += f"- {content}: file size = {file_size}, is in dir = {is_dir}\n"
        
    
    return result

def get_file_content(working_dir: str, file_path: str) -> str:
    abs_working_dir: str = os.path.abspath(working_dir)
    abs_file_path: str = os.path.abspath(os.path.join(working_dir, file_path))

    if (not abs_file_path.startswith(abs_working_dir)):
        return f'Error: Cannot read "{file_path}" as it is outside working directory'
    
    if (not os.path.isfile(abs_file_path)):
        return f'Error: File path provided does not point to file: "{file_path}"'
    
    result: str = ""
    with open(abs_file_path, "r") as file:
        result = file.read(10000)
        
    return result

schema_get_files_info = FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=Schema(
        type=types.Type.OBJECT,
        properties={
            "dir": Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = FunctionDeclaration(
    name="get_file_content",
    description="Reads out the content of the given file as a string, constrained to the working directory.",
    parameters=Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": Schema(
                type=types.Type.STRING,
                description="The path to the file that will be read, from the working directory.",
            )
        },
    ),
)