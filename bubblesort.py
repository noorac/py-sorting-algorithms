# Bubble Sort
from timer import timer


@timer
def bubblesort(sortlist) -> list:
    """
    Bubble sort:
    Bubble Sort repeatedly steps through the array, compares adjacent elements,
    and swaps them if they are out of order. This process continues until the
    array is sorted.
    Time complexity: All cases O(n^2) (except if it is already sorted O(n))
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
    sortedlist, elapsedtime = bubblesort(listtosort)
    print(f"Sorted:{sortedlist}")
    print(f"Time elapsed: {elapsedtime} seconds")
    return None


if __name__ == "__main__":
    main()
