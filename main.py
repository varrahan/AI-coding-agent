import os
import sys
from dotenv import load_dotenv
from google.genai import Client, types
from google.genai.types import GenerateContentResponse, Content, Part
from functions.get_files import schema_get_file_content, schema_get_files_info
from functions.write_files import schema_write_file
from functions.run import schema_run_python
from call_functions import call_function

def main() -> int:
    load_dotenv()
    
    api_key: str | None = os.getenv("API_KEY")
    client: Client = Client(api_key=api_key)
    verbose: bool = False
    system_prompt: str = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories
        - Read file contents
        - Execute Python files with optional arguments
        - Write or overwrite files

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """ 

    if (len(sys.argv) < 2):
        print("Missing arguement: prompt")
        return 1
    
    if (len(sys.argv) <= 4 and sys.argv[-1] == "--verbose"):
        verbose = True
    
    prompt: str = sys.argv[1]
    
    messages: list[Content] = [
        Content(role="user", parts=[Part(text=prompt)])
    ]
    
    available_functions: types.Tool = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python,
        schema_write_file
        ]
    )   
    
    MAX_ITERATIONS: int = 30
    for _ in range(0, MAX_ITERATIONS):
        
        response: GenerateContentResponse = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], 
                system_instruction=system_prompt
            )
        )
        
        if response.candidates:
            for candidate in response.candidates:
                if candidate.content is None:
                    continue
                messages.append(candidate.content)
        
        if response.function_calls:
            for function_call_part in response.function_calls:
                result: Content = call_function(function_call_part, verbose)
                messages.append(result)
        else:
            print(response.text)
            return 0

        if response.usage_metadata is None:
            print("Response is malformed")
        
        if verbose:
            print("Prompt tokens:", [response.usage_metadata.prompt_token_count])
            print("Response tokens:", [response.usage_metadata.candidates_token_count])
            
        
    return 0

if __name__ == "__main__":
    main()