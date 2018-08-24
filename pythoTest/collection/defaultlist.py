from collections import defaultdict

ret = defaultdict(list)
ret[123].append("123:1")
ret[123].append("123:2")
ret[123].append("123:3")
ret[124].append("124:1")
ret[124].append("124:2")
ret[124].append("124:3")

print("type(ret)={}".format(type(ret)))
for i in ret:
    print("type{} {}".format(type(i), type(ret[i])))
    print("value {} {}".format(i, ret[i]))
