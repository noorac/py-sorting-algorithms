# Bubble Sort
from timer import timer


@timer
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

    listtosort = argvlist(argv[1:])
    if len(listtosort) == 0:
        from testlist import test_list

        # using test_list, def. 15 000
        listtosort = test_list()
    print(f"Unsorted:{listtosort}")
    sortedlist, elapsedtime = bubblesort(listtosort)
    print(f"Sorted:{sortedlist}")
    print(f"Time elapsed: {elapsedtime} seconds")
    return None


if __name__ == "__main__":
    main()
