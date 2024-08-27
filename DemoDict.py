# DimoDict.py

# 사전식 구조

colors = {"apple":"red","banana":"yellow"}

print(colors)

print(len(colors))

#검색

print(colors["apple"])
print(colors)

#수정
colors["cherry"]= "pink"
print(colors)

colors["apple"]= "blue"
print(colors)

#del colors["banana"]
#print(colors)

print('---반복분 time----')
for a in colors.items():
    print(type(a))
    print(a)

for i,v in colors.items():
    print(type(i),type(v))
    print(v,i)

isRight = False
print(type(isRight))

print(1<2)

print(1==2)

print(True or False or False)
print(True and False and False)


# 0 이 False  0이 아니면 True

print(bool(None))
print(bool([]))
print(bool(None))

print (bool(0 and 0))

