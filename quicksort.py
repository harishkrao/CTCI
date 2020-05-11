class quicksort:
    def quicksort(self, array, lo, hi):
        if lo >= hi:
            return
        p = self.partition(array, lo, hi)
        self.quicksort(array, lo, p-1)
        self.quicksort(array, p+1, hi)

    def partition(self, array, lo, hi):
        v = array[lo]
        start = lo + 1
        end = hi

        while True:
            while start <= end and array[start] <= v:
                start += 1
            while start <= end and array[end] >= v:
                end -= 1
            if start > end:
                break
            else:    
                array[start], array[end] = array[end], array[start]
        array[lo], array[end] = array[end], array[lo]
        return end


def main():
    array = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
    q = quicksort()
    q.quicksort(array, 0, len(array)-1)
    print(array)


if __name__ == "__main__":
    main()
