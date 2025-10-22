import os
import subprocess
from google.genai import types
from google.genai.types import FunctionDeclaration, Schema

def run_python(working_dir: str, file_path: str, args: list[str] = []) -> str:
    abs_working_dir: str = os.path.abspath(working_dir)
    abs_file_path: str = os.path.abspath(os.path.join(working_dir, file_path))

    if (not abs_file_path.startswith(abs_working_dir)):
        return f'Error: Cannot read "{file_path}" as it is outside working directory'
    
    if (not os.path.isfile(abs_file_path)):
        return f'Error: File path provided does not point to file: "{file_path}"'
    
    if (not abs_file_path.endswith(".py")):
        return f'Error: File path provided does not point to a python file: "{file_path}"'
    
    try:
        commands: list[str] = ["python3", file_path ] + args
        result = subprocess.run(commands, 
                                cwd=abs_working_dir,
                                capture_output=True, 
                                timeout=30)
        return f"""
            STDOUT: {result.stdout}
            STDERR: {result.stderr}
            Process exited with code {result.returncode}
        """
    except Exception as ex:
        return f"Exception has occured in the run_python function: {ex}"
    
schema_run_python = FunctionDeclaration(
    name="run_python",
    description="Runs a python file with the python3 interpreter. Accepts additional CLI args as an optional array.",
    parameters=Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": Schema(
                type=types.Type.STRING,
                description="The path to the file that will be read, from the working directory.",
            ),
            "args": Schema(
                type=types.Type.ARRAY,
                description="An optional array of strings to be used as CLI args for the python file",
                items=types.Schema(
                    type=types.Type.STRING,
                )
            )
        },
    ),
)


    