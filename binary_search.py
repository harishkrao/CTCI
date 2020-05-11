def binary_search(search_element, array):
    if len(array) == 1:
        if array[0] == search_element:
            return 'found'
        else:
            return 'not found -- came down to the last element'
    elif len(array) > 1:
        mid = len(array)//2
        if search_element == array[mid]:
            return 'found'
        elif search_element > array[mid]:
            return binary_search(search_element, array[mid+1:])
        elif search_element < array[mid]:
            return binary_search(search_element, array[:mid])
        else:
            return 'not found in array'
    else:
        return 'not found -- array became empty'


array = [12, 19, 21, 27, 28, 29, 31, 41, 44, 44, 58, 97, 99]

tests = [10, 12, 19, 27, 30, 31, 44, 78, 99, 100, 120]
for vals in tests:
    print(vals, binary_search(vals,array))
