# class1.py

#1)클래스를 정의

class Person:
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
    
    def print(self):
        print("My name is {0}".format(self.name))

# 인스턴스생성
p1= Person()
p1.name ="csh"


p2 = Person()
# 메서드 호출


p1.print()
p2.print()