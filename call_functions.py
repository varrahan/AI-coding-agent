from os import getcwd
from json import loads, JSONDecodeError
from functions.get_files import get_file_content, get_files_info
from functions.write_files import write_file
from functions.run import run_python
from google.genai.types import Content, FunctionCall, Part
from typing import Any

working_dir = getcwd()

def call_function(function_call_part: FunctionCall, verbose: bool = False) -> Content:
    
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
        
    args: dict[str, Any] = {}
    if isinstance(function_call_part.args, str):
        try:
            args = loads(function_call_part.args)
        except JSONDecodeError:
            print(f"Error decoding function call arguements: {function_call_part.args}")
    elif isinstance(function_call_part.args, dict):
        args = function_call_part.args

    result: str = ""
    if function_call_part.name ==  "get_file_content":
        result = get_file_content(working_dir, **args)
    elif function_call_part.name ==  "get_files_info":
        result = get_files_info(working_dir, **args)
    elif function_call_part.name == "write_file":
        result = write_file(working_dir, **args)   
    elif function_call_part.name == "run_python":
        result = run_python(working_dir, **args)
    else: 
        return Content(
            role="tool",
            parts=[
                Part.from_function_response(
                    name=function_call_part.name or "",
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )
    return Content(
        role="tool",
        parts=[
            Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )

    