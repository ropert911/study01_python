# 定义函数
def printme( str ):
    "打印任何传入的字符串"
    print(str)
    return;

# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");


#整数、字符串、元组 传递的是值对象
def ChangeInt( a ):
    a = 10

b = 2
ChangeInt(b)
print(b)


# 可写函数说明
def changeme( mylist ):
    "修改传入的列表"
    mylist.append([1,2,3,4]);
    print("函数内取值: ", mylist)
    return

# 调用changeme函数
mylist = [10,20,30];
changeme(mylist );
print("函数外取值: ", mylist)



#指标使用参数
def printinfo( name, age ):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return;

printinfo(age=50, name="miki");




#缺省参数=================================
def printinfo(name, age = 35):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return;

#调用printinfo函数
printinfo(age=50, name="miki");
printinfo(name="miki");


#不定长参数：加了星号（*）的变量名会存放所有未命名的变量参数===============
def printinfo( arg1, *vartuple ):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return;

# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);



#匿名函数===================== lambda只是一个表达式，函数体比def简单很多
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print("相加后的值为 : ", sum( 10, 20 ))
print("相加后的值为 : ", sum( 20, 20 ))