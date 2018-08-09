import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口

s.listen(5)                 # 等待客户端连接
while True:
    c, addr = s.accept()     # 建立客户端连接。
    print('连接地址：', addr)
    c.send(bytes('欢迎访问菜鸟教程！', encoding = "utf8"))
    c.close()                # 关闭连接

"""
s = "example"           # str object
bytes(s, encoding = "utf8")         # str to bytes

b = b"example"              # bytes object
str(b, encoding = "utf-8")      # bytes to str

# an alternative method
# str to bytes
str.encode(s)

# bytes to str
bytes.decode(b)
"""