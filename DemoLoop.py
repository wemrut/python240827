#Demo


value = 5

while value > 0:
    print(value)
    value = value -1

print("--- for in 루프---")

lst = [10,20,30]

for i in lst:
    print("item:{0}".format(i))

print("---range()---")

lst = list(range(10))

print(lst)
print([i**2 for i in lst if i>5])

print(list(range(2000,2025)))

print(list(range(1,32)))


# 필터링 함수

print("--필터링함수---")

let = [10,25,30]
iterL = filter(None,let)

for item in iterL:
    print(item)

def getBiggerThan20(i):
    
    return i>20

let = [10,25,30]
iterL = filter(getBiggerThan20,let)

for item in iterL:
    print(item)


print("---람다함수 사용---")

iterL = filter(lambda x:x>20,let)

for item in iterL:
    print(item)