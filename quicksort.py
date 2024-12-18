# Quicksort
from timer import timer


def partition(sortlist, low, high):
    # Using last element as pivot
    pivot = sortlist[high]
    i = low - 1
    for j in range(low, high):
        if sortlist[j] < pivot:
            i += 1
            swapindex(sortlist, i, j)
    swapindex(sortlist, i + 1, high)
    return i + 1


def swapindex(sortlist, i, j):
    sortlist[i], sortlist[j] = sortlist[j], sortlist[i]


@timer
def quicksort(sortlist, low=None, high=None) -> list:
    """
    Quicksort:
    Works by chosing a pivot and dividing into subarrays, then recursively sort the subarrays.
    Time complexity: 
    Best: O(n*log n)
    Worst: O(n^2)
    Average: O(n*log n)
    """
    if low is None:
        low = 0
    if high is None:
        high = len(sortlist) - 1
    if low < high:
        pi = partition(sortlist, low, high)
        quicksort(sortlist, low, pi - 1)
        quicksort(sortlist, pi + 1, high)
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
    sortedlist, elapsedtime = quicksort(listtosort)
    print(f"Sorted:{sortedlist}")
    print(f"Time elapsed: {elapsedtime} seconds")
    return None


if __name__ == "__main__":
    main()
