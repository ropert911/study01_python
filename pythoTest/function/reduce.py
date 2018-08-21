from functools import reduce

list1 = [1, 2, 3, 4, ]
list1 = reduce(lambda a, b: a + b, list1) if list1 else 0
print(list1)

list2 = [(1, 1), (2, 2), (3, 3), (4, 4)]
list2 = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), list2) if list2 else [(0, 0)]
print(list2)
