# Bubble Sort
from timer import timer


@timer
def mergesort(sortlist) -> list:
    """
    Mergesort: Mergesort divides the array into halves, recursively sorts them,
    and merges the sorted halves into a single sorted array.
    Time complexity: 
    Best: All cases O(n*log(n))
    """
    if len(sortlist) < 2:
        return sortlist
    center = len(sortlist) // 2
    left, _ = mergesort(sortlist[:center])
    right, _ = mergesort(sortlist[center:])
    sorted = merge(left, right)
    return sorted


def merge(left, right) -> list:
    if not len(left):
        return left
    if not len(right):
        return right

    res = []
    indexleft = 0
    indexright = 0
    totallength = len(left) + len(right)

    while len(res) < totallength:
        if left[indexleft] < right[indexright]:
            res.append(left[indexleft])
            indexleft += 1
        else:
            res.append(right[indexright])
            indexright += 1

        if indexleft == len(left) or indexright == len(right):
            res.extend(left[indexleft:] or right[indexright:])
            break
    return res


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
    sortedlist, elapsedtime = mergesort(listtosort)
    print(f"Sorted:{sortedlist}")
    print(f"Time elapsed: {elapsedtime} seconds")
    return None


if __name__ == "__main__":
    main()
