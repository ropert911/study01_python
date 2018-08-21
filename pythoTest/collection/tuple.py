#元组是不能修改的

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print("tup1: ", tup1)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

tup3 = tup1 + tup2
print("新的元组",tup3)
del tup3         #删除