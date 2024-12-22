# Heapsort
from timer import timer


def heapify(sortlist, listlength, i):
    greatest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < listlength and sortlist[i] < sortlist[left]:
        greatest = left
    if right < listlength and sortlist[greatest] < sortlist[right]:
        greatest = right
    if greatest != i:
        sortlist[i], sortlist[greatest] = sortlist[greatest], sortlist[i]
        heapify(sortlist, listlength, greatest)


@timer
def heapsort(sortlist) -> list:
    """
    Heapsort: Heapsort builds a max heap from the array, then repeatedly swaps the
    root (largest) with the last element, reduces the heap size, and re-heaps the
    remaining elements.
    Time complexity: All cases O(n*log(n))
    """
    sortlist.insert(0,"test")
    listlength = len(sortlist)
    for i in range(listlength, 0, -1):
        heapify(sortlist, listlength, i)
    for i in range(listlength - 1, 0, -1):
        sortlist[i], sortlist[0] = sortlist[0], sortlist[i]
        heapify(sortlist, i, 0)
    sortlist.pop(-1)
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
    sortedlist, elapsedtime = heapsort(listtosort)
    print(f"Sorted:{sortedlist}")
    print(f"Time elapsed: {elapsedtime} seconds")
    return None


if __name__ == "__main__":
    main()
