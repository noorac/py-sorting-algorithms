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
        while currentminindex > 0 and currentmin < sortlist[currentminindex-1]:
            sortlist[currentminindex] = sortlist[currentminindex-1]
            currentminindex -= 1
        sortlist[currentminindex] = currentmin
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
    print(f"Sorted:{insertionsort(listtosort)}")
    print(f"Time elapsed:{endtime-starttime}")
    return None


if __name__ == "__main__":
    main()
