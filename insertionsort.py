# Insertion Sort


def insertionsort(sortlist) -> list:
    """
    Insertion sort:
    Works by iterating the list, "picking up" the next number, working
    backwards inserting the next number when it is no longer smaller
    than the number it checks.
    Time complexity: O(n^2)
    """
    for i in range(len(sortlist)):
        # i is index to start at
        currentmin = sortlist[i]
        currentminindex = i
        while currentminindex > 0 and currentmin < sortlist[currentminindex - 1]:
            sortlist[currentminindex] = sortlist[currentminindex - 1]
            currentminindex -= 1
        sortlist[currentminindex] = currentmin
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
    print(f"Sorted:{insertionsort(listtosort)}")
    endtime = time()
    getcontext().prec = 3
    print(f"Time elapsed:{Decimal(endtime)-Decimal(starttime)} seconds")
    return None


if __name__ == "__main__":
    main()
