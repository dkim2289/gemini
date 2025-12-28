from functions.write_files import write_file


def test():
    r = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("result:")
    print(r + "\n")

    r = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("result:")
    print(r + "\n")

    r = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("result:")
    print(r + "\n")


if __name__ == "__main__":
    test()
