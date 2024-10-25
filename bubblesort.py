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
    from sys import argv
    from argvlist import argvlist
    from time import time
    starttime = time()
    listtosort = argvlist(argv[1:])
    endtime = time()
    print(f"Unsorted:{listtosort}")
    print(f"Sorted:{bubblesort(listtosort)}")
    print(f"Time elapsed:{endtime-starttime}")
    return None


if __name__ == "__main__":
    main()
