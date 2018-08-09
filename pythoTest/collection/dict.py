dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
# print("dict['Alice']: ", dict['Alice'])



dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School"; # Add new entry
print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
dict.setdefault("Name","aaa")               #setdefault() 如果键不存在于字典中，将会添加键并将值设为默认值
print("dict['Name']: ",dict['Name'])



dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};

del dict['Name']; # 删除键是'Name'的条目
dict.clear();     # 清空词典所有条目
del dict ;        # 删除词典

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
