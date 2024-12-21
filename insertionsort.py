# Insertion Sort
from timer import timer


@timer
def insertionsort(sortlist) -> list:
    """
    Insertion sort: Insertion Sort builds a sorted portion of the array by repeatedly picking
    the next element and inserting it into its correct position within the sorted part.
    Time complexity: All cases O(n^2) (except already sorted, which is O(n))
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
    sortedlist, elapsedtime = insertionsort(listtosort)
    print(f"Sorted:{sortedlist}")
    print(f"Time elapsed: {elapsedtime} seconds")
    return None


if __name__ == "__main__":
    main()
