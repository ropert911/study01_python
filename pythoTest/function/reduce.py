from collections import namedtuple
from functools import reduce

user1 = {'userId': 1, 'topAreaList': [12, 13, 14]}
user2 = {'userId': 2, 'topAreaList': [22, 23, 24]};
user_list = [user1, user2];

UserWithArea = namedtuple('UserWithArea', ('id', 'top_areas'))

user_list = [UserWithArea(user['userId'], [_ for _ in user['topAreaList']]) for user in user_list]

print(user_list)

list1=[(1,1),(2,2),(3,3),(4,4)]
# 如果用户没有一级区域，则所有数据全部置为0
list1 = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]), list1) if list1 else [(0,0)]
print(list1)
