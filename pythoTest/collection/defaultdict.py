from collections import defaultdict

ret = defaultdict(list)
ret[123].append("123:1")
ret[123].append("123:2")
ret[123].append("123:3")
ret[124].append("124:1")
ret[124].append("124:2")
ret[124].append("124:3")
ret["aa"].append("aaa")

for i in ret:
    print("{} {}====={} {}".format(type(i), type(ret[i]), i, ret[i]))

bag = ['apple', 'orange', 'cherry', 'apple', 'apple', 'cherry', 'blueberry']
count = defaultdict(int)
for fruit in bag:
    count[fruit] += 1
for i in count:
    print("value {}  {}".format(i, count[i]))
