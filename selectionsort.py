# Selection Sort
from timer import timer


@timer
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
    from sys import argv

    from testlist import test_list

    try:
        # listlength = int(argvlist(argv[1]))
        listlength = int(argv[1])
    except IndexError:
        listlength = 15000
    except ValueError:
        listlength = 15000
    # using test_list, def. 15 000
    listtosort = test_list(listlength)
    print(f"Unsorted:{listtosort}")
    sortedlist, elapsedtime = selectionsort(listtosort)
    print(f"Sorted:{sortedlist}")
    print(f"Time elapsed: {elapsedtime} seconds")
    return None


if __name__ == "__main__":
    main()
