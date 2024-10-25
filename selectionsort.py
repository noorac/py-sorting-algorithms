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
        for j in range(i,i+len(sortlist[i:])):
            if currentmin > sortlist[j]:
                currentmin = sortlist[j]
                currentminindex = j
        sortlist.pop(currentminindex)
        sortlist.insert(i,currentmin)
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
    print(f"Sorted:{selectionsort(listtosort)}")
    print(f"Time elapsed:{endtime-starttime}")
    return None


if __name__ == "__main__":
    main()
