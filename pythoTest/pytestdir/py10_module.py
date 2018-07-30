# 导入模块
import support

# 现在可以调用模块里包含的函数了
support.print_func("Runoob")
print(dir(support))

#from…import 语句
#Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
#from fib import fibonacci
#这个声明不会把整个 fib 模块导入到当前的命名空间中，它只会将 fib 里的 fibonacci 单个引入到执行这个声明的模块的全局符号表


#搜索路径
"""当你导入一个模块，Python 解析器对模块位置的搜索顺序是：
1、当前目录
2、如果不在当前目录，Python 则搜索在 shell 变量 PYTHONPATH 下的每个目录。
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一般为/usr/local/lib/python/。"""
"""在 Windows 系统，典型的 PYTHONPATH 如下：
set PYTHONPATH=c:\python27\lib;
在 UNIX 系统，典型的 PYTHONPATH 如下：
set PYTHONPATH=/usr/local/lib/python"""


#命名空间和作用域====================
Money = 2000
def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1

print(Money)
AddMoney()
print(Money)