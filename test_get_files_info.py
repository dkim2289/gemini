from functions.get_files_info import get_files_info


def debug_test():
    result = get_files_info("calculator", ".")
    print(f"Result for current directory:")
    print(result + "\n")

    result = get_files_info("calculator", "pkg")
    print(f"Result for current directory:")
    print(result + "\n")

    result = get_files_info("calculator", "/bin")
    print(f"Result for current directory:")
    print(result + "\n")

    result = get_files_info("calculator", "../")
    print(f"Result for current directory:")
    print(result + "\n")


if __name__ == "__main__":
    debug_test()
