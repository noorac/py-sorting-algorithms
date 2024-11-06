# Test list


def test_list(length=15000) -> list:
    """
    Generates a list of random numbers with length length
    """
    import random

    return_list = []
    for _ in range(length):
        return_list.append(random.randrange(0, length, 1))
    return return_list


def main() -> None:
    print(f"{test_list()}")
    return None


if __name__ == "__main__":
    main()
