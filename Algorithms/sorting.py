def bubble_sort(arr: list, reverse: bool = False):
    for j in range(len(arr), 1, -1):
        for i in range(1, j):
            if reverse:
                if arr[i] > arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
            else:
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
    return arr


def selection_sort(arr: list, reverse: bool = False):
    for i in range(0, len(arr) - 1):
        minimum = arr[i]
        for j in range(i, len(arr)):
            if reverse:
                if arr[j] < minimum:
                    minimum, arr[j] = arr[j], minimum
            else:
                if arr[j] < minimum:
                    minimum, arr[j] = arr[j], minimum
        arr[i], minimum = minimum, arr[i]
    return arr


def merge_sort(arr: list, reverse: bool = False):
    pass


def quick_sort(arr: list, reverse: bool = False):
    pass
