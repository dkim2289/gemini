import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        awd = os.path.abspath(working_directory)
        afp = os.path.normpath(os.path.join(awd, file_path))
        if awd != os.path.commonpath([awd, afp]):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(afp):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(afp), exist_ok=True)
        with open(afp, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="write or overwrite (within limits)",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path of the file to get the content of",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="new content to be written or overwritten"
            ),
        },
        required=["file_path","content"],
    ),
)
