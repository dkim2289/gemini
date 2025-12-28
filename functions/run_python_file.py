import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    try:
        awd = os.path.abspath(working_directory)  # absolute working directory
        afp = os.path.normpath(os.path.join(awd, file_path))  # absolute file path
        if awd != os.path.commonpath([awd, afp]):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(afp):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if ".py" not in afp:
            return f'Error: "{file_path}" is not a Python file'
        c = ["python", afp]  # command
        if args:
            c.extend(args)
        cp = subprocess.run(  # completed process
            c, cwd=awd, capture_output=True, text=True, timeout=30
        )
        op = []  # output (string)
        if cp.returncode != 0:
            op.append(f"Process exited with code {cp.returncode}")
        if not cp.stdout and not cp.stderr:
            op.append("No output produced")
        else:
            if cp.stdout:
                op.append(f"STDOUT: {cp.stdout}")
            if cp.stderr:
                op.append(f"STDERR: {cp.stderr}")
        return "\n".join(op)

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="run arbitrary Python code",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="file path of the file to get the content of",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="has items that are string",
            ),
        },
        required=["file_path"],
    ),
)
