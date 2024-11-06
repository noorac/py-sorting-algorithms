# Selection Sort


def selectionsort(sortlist) -> list:
    """
    Selection sort:
    Works by iterating the list, remembering what is the lowest number, puttin
    it at the front of the list, then starting again at index 2.
    Time complexity: O(n^2)
    """
    for i in range(len(sortlist)):
        # i is index to start at
        currentmin = sortlist[i]
        currentminindex = i
        for j in range(i, i + len(sortlist[i:])):
            if currentmin > sortlist[j]:
                currentmin = sortlist[j]
                currentminindex = j
        sortlist.pop(currentminindex)
        sortlist.insert(i, currentmin)
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
    print(f"Sorted:{selectionsort(listtosort)}")
    endtime = time()
    getcontext().prec = 3
    print(f"Time elapsed:{Decimal(endtime)-Decimal(starttime)} seconds")
    return None


if __name__ == "__main__":
    main()
