# Shell sort
from timer import timer


@timer
def shellsort(sortlist) -> list:
    """
    Shell sort:
    Time complexity: 
    Best: O(n*log(n))
    Average: O(n*log(n))
    Worst: O(n^2)
    """
    listlength = len(sortlist)
    gapsize = listlength//2
    while gapsize > 0:
        for i in range(gapsize,listlength):
            check = sortlist[i]
            j = i
            while j >= gapsize and sortlist[j-gapsize] > check:
                sortlist[j] = sortlist[j-gapsize]
                j -= gapsize
            sortlist[j] = check
        gapsize //= 2

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
    sortedlist, elapsedtime = shellsort(listtosort)
    print(f"Sorted:{sortedlist}")
    print(f"Time elapsed: {elapsedtime} seconds")
    return None


if __name__ == "__main__":
    main()
