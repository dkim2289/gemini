import os

from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    try:
        awd = os.path.abspath(working_directory)
        afp = os.path.normpath(os.path.join(awd, file_path))
        if os.path.commonpath([awd, afp]) != awd:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(afp):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(afp, "r") as f:
            file_cont_str = f.read(MAX_CHARS)
            if f.read(1):
                file_cont_str += (
                    f'\n\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return file_cont_str
    except Exception as e:
        return f"Error: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="get the contents of a file of a directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path of the file to get the content of",
            ),
        },
        required=["file_path"],
    ),
)
