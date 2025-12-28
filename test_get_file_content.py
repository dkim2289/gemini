from functions.get_files_content import get_file_content


def debug_test():
    result = get_file_content("calculator", "lorem.txt")
    print(f"Result for current file content:")
    print(result + "\n")

    result = get_file_content("calculator", "main.py")
    print(f"Result for current file content:")
    print(result + "\n")

    result = get_file_content("calculator", "pkg/calculator.py")
    print(f"Result for current file content:")
    print(result + "\n")

    result = get_file_content("calculator", "/bin/cat")
    print(f"Result for current file content:")
    print(result + "\n")

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"Result for current file content:")
    print(result + "\n")


if __name__ == "__main__":
    debug_test()
