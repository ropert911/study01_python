if isinstance(1, int):
    print("true :   isinstance (1,int)")
else:
    print("false :   isinstance (1,int)")

if isinstance("aaaa", str):
    print("true :   isinstance (1,str)")
else:
    print("false :   isinstance (1,str)")

# 默认和空格分开
para = "aaa=bbb bbb=ccc aaa"
spaceResult = para.split()
print("分割后=%s  " % (spaceResult))
equalResult = filter(lambda item: "=" in item, spaceResult)
equalResultList = list(equalResult)
print("等号过滤后=%s" % equalResultList)
mapResult = map(lambda item: item.split("="), equalResultList)
mapResultList = list(mapResult)
print("按=号split做map后=%s" % mapResultList)
dictResult = dict(mapResultList)
print("最后生成的字典=%s" % dictResult)
for key in dictResult.keys():
    print(key + ':' + dictResult[key])
