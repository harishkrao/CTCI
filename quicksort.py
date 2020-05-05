import random

def sort(a, lo, hi):
    if lo >= hi:
        return
    p = partition(a, lo, hi)
    sort(a, lo, p-1)
    sort(a, p+1, hi)


def partition(a, lo, hi):
    start = lo + 1
    end = hi
    pivot = a[lo]

    while True:
        while start <= end and a[start] <= pivot:
            start += 1
        while start <= end and a[end] >= pivot:
            end -= 1
        if lo <= hi:
            a[start], a[end] = a[end], a[start]
        else:
            break
    a[lo], a[end] = a[end], a[lo]
    return end


a = ['Q', 'U', 'I', 'C', 'K', 'S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
random.shuffle(a)
sort(a, 0, len(a)-1)
print(a)
