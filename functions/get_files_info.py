import os

from google.genai import types


def get_files_info(working_directory, directory="."):
    try:
        awd = os.path.abspath(working_directory)
        atd = os.path.normpath(os.path.join(awd, directory))
        if os.path.commonpath([awd, atd]) != awd:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(atd):
            return f'Error: "{directory}" is not a directory'
        items_data = []
        for item in os.listdir(atd):
            item_full_path = os.path.join(atd, item)
            items_data.append(
                f"- {item}: file_size={os.path.getsize(item_full_path)} bytes, is_dir={os.path.isdir(item_full_path)}"
            )
        return "\n".join(items_data)
    except Exception as e:
        return f"Error: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
