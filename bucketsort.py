# Bucketsort
# This bucketsort is completely rudinetary, it needs strengthening and updating
from timer import timer


@timer
def bucketsort(sortlist) -> list:
    """
    Bucket sort:
    Time complexity:
    Best: O(n+k)
    Average: O(n)
    Worst: O(n^2)
    """
    retlist = []
    bucket = [[] for _ in range(len(sortlist))]

    for number in sortlist:
        bucket[number].append(number)

    for ibucket in bucket:
        if ibucket is not None:
            for jbucket in ibucket:
                retlist.append(jbucket)
    sortlist = retlist

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
    sortedlist, elapsedtime = bucketsort(listtosort)
    print(f"Sorted:{sortedlist}")
    print(f"Time elapsed: {elapsedtime} seconds")
    return None


if __name__ == "__main__":
    main()
