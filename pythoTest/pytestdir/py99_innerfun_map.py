# map 映射函数
def f(x):
    return x * x


l1 = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("list1")
for i in l1:
    print(i)

l2 = map(lambda x, y: x ** y, [1, 2, 3], [1, 2, 3])  # n的m次方
print("list2")
for i in l2:
    print(i)

l3 = map(lambda x, y: (x ** y, x + y), [1, 2, 3], [1, 2, 3])
print("list3")
for i in l3:
    print(i, "type=", type(i))

l4 = map(lambda x, y: (x ** y, x + y), [1, 2, 3], [1, 2])
print("list4")
for i in l4:
    print(i, "type=", type(i))
