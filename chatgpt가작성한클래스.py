# Person 클래스 정의
class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        #print("Info(ID:{0}, Name: {1})".format(self.ID, self.Name)) 랑 같은 코드
        print(f"ID: {self.id}, Name: {self.name}")

# Manager 클래스 정의 (Person을 상속)
class Manager(Person):
    def __init__(self, id, name, title):
        # 부모 클래스 재정의
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

# Employee 클래스 정의 (Person을 상속)
class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

# 테스트 코드
def test_code():
    # 테스트 1: Person 클래스 인스턴스 생성 및 정보 출력
    person1 = Person(1, "Alice")
    person1.printInfo()  # ID: 1, Name: Alice

    # 테스트 2: Manager 클래스 인스턴스 생성 및 정보 출력
    manager1 = Manager(2, "Bob", "Project Manager")
    manager1.printInfo()  # ID: 2, Name: Bob, Title: Project Manager

    # 테스트 3: Employee 클래스 인스턴스 생성 및 정보 출력
    employee1 = Employee(3, "Charlie", "Python Developer")
    employee1.printInfo()  # ID: 3, Name: Charlie, Skill: Python Developer

    # 테스트 4: Person 클래스의 id와 name 변경 후 출력
    person1.id = 10
    person1.name = "Alice Updated"
    person1.printInfo()  # ID: 10, Name: Alice Updated

    # 테스트 5: Manager 클래스의 title 변경 후 출력
    manager1.title = "Senior Project Manager"
    manager1.printInfo()  # ID: 2, Name: Bob, Title: Senior Project Manager

    # 테스트 6: Employee 클래스의 skill 변경 후 출력
    employee1.skill = "Java Developer"
    employee1.printInfo()  # ID: 3, Name: Charlie, Skill: Java Developer

    # 테스트 7: 새로운 Person 인스턴스 생성 및 정보 출력
    person2 = Person(4, "Dave")
    person2.printInfo()  # ID: 4, Name: Dave

    # 테스트 8: 새로운 Manager 인스턴스 생성 및 정보 출력
    manager2 = Manager(5, "Eve", "HR Manager")
    manager2.printInfo()  # ID: 5, Name: Eve, Title: HR Manager

    # 테스트 9: 새로운 Employee 인스턴스 생성 및 정보 출력
    employee2 = Employee(6, "Frank", "Data Scientist")
    employee2.printInfo()  # ID: 6, Name: Frank, Skill: Data Scientist

    # 테스트 10: 각 클래스의 printInfo 메서드가 올바르게 동작하는지 반복 테스트
    for obj in [person1, manager1, employee1, person2, manager2, employee2]:
        obj.printInfo()

# 테스트 코드 실행
test_code()
