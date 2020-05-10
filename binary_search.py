def binary_search(array, search_element):
    

array = [12, 19, 21, 27, 28, 29, 31, 41, 44, 44, 58, 66, 76, 78, 83, 87, 88, 97, 99]

tests = [10, 12, 18, 21, 28, 15, 27, 30, 29, 44, 59, 66, 76, 80, 85, 87, 95, 99, 100, 120]
for vals in tests:
    print(vals, binary_search(vals, array))
