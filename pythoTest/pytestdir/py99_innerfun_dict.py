# dict 字典
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print("dict['Name']: ",dict['Name'])
print("dict['Age']: ", dict['Age'])
#setdefault() 函数和get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值
dict.setdefault("Name","aaa")
print("dict['Name']: ",dict['Name'])
