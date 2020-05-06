# class quicksort:
def qsort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    qsort(array, start, p - 1)
    qsort(array, p + 1, end)


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]

    return high


array = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
qsort(array, 0, len(array) - 1)
print(array)
