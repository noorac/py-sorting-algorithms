# Bubble Sort


def bubblesort(sortlist) -> list:
    """
    Bubble sort:
    Works by swapping a list item with the following item if it if bigger
    than the next item.
    Time complexity: O(n^2)
    """
    for i in range(len(sortlist)):
        s = False
        for j in range(0, len(sortlist) - i - 1):
            if sortlist[j] > sortlist[j + 1]:
                sortlist[j], sortlist[j + 1] = sortlist[j + 1], sortlist[j]
                s = True
        if s is False:
            break

    return sortlist


def main() -> None:
    """
    Use main by giving a set of numbers after the filename
    separated by a comma.
    """
    from decimal import Decimal, getcontext
    from sys import argv
    from time import time

    from argvlist import argvlist

    listtosort = argvlist(argv[1:])
    if len(listtosort) == 0:
        from testlist import test_list

        # using test_list, def. 15 000
        listtosort = test_list()
    print(f"Unsorted:{listtosort}")
    starttime = time()
    print(f"Sorted:{bubblesort(listtosort)}")
    endtime = time()
    getcontext().prec = 3
    print(f"Time elapsed:{Decimal(endtime)-Decimal(starttime)} seconds")
    return None


if __name__ == "__main__":
    main()
