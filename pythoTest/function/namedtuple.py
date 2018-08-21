from collections import namedtuple

user1 = {'userId': 1, 'topAreaList': [12, 13, 14]}
user2 = {'userId': 2, 'topAreaList': [22, 23, 24]};
user_list = [user1, user2];

UserWithArea = namedtuple('UserWithArea', ('id', 'top_areas'))
user_list = [UserWithArea(user['userId'], [_ for _ in user['topAreaList']]) for user in user_list]

print(user_list)
