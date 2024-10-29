# Argvlist, a script that turns a list of argv arguments into a list of integers


def argvlist(listtoconvert) -> list:
    """
    Makes an attempt at turning the elements of a list into
    integers. In case of ValueError, exit the program.
    """
    for i in range(len(listtoconvert)):
        try:
            listtoconvert[i] = int(listtoconvert[i])
        except ValueError:
            print(f"ValueError: Check arguments")
            exit()
    return listtoconvert


def main() -> None:
    from sys import argv

    listtosort = argvlist(argv[1:])
    print(f"Converted list:{listtosort}")
    return None


if __name__ == "__main__":
    main()
