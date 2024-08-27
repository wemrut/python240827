strName = "Not Class Member"

class DemoString:
    def __init__(self):
        #인스턴스 멤버 변수 초기화
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        #print(strName)
        #버그 발생(파이썬은 명확한 것이 좋다!)
        print(self.strName)

#인스턴스 생성
d = DemoString()
d.set("First Message")

# 인스턴스가 FirstMessage로 나와야 하는데 전역변수가 선언됨
d.print()


i=1
print(i)

