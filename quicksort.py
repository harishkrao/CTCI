class quicksort:
    def __init__(self, array):
        self.array = array

    def qsort(self, array, lo, hi):
        if lo >= hi:
            return
        p = self.partition(array, lo, hi)
        self.qsort(array, lo, p-1)
        self.qsort(array, p+1, hi)

    def partition(self, array, lo, hi):
        pivot = array[lo]
        start = lo + 1
        end = hi

        while True:
            while start <= end and array[start] <= pivot:
                start += 1
            print(start, end, array)
            while start <= end and array[end] >= pivot:
                end -= 1
            if start <= end:
                array[start], array[end] = array[end], array[start]
            else:
                break
        print(start, end)
        array[end], array[lo] = array[lo], array[end]
        return end


def main():
    array = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
    q = quicksort(array)
    q.qsort(array, 0, len(array)-1)
    print(array)


if __name__ == "__main__":
    main()