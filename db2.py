# db1.py
import sqlite3

#연결객체 생성(처음에는 메모리에만 저장)
#con = sqlite3.connect(":memory:")

#파일에 저장(IDLE같이 연습)
con = sqlite3.connect(r"c:\work\sample.db")
#sql구문을 실행하는 커서 객체 생성
cur = con.cursor()

# PhoneBook Table이 없으면 만들어
cur.execute("create table if not exists PhoneBook (Name text,PhoneNum text);")



# 입력구분

# cur.execute("insert into PhoneBook values ('derick','010-111');")

# 검색구문


#입력 매개변수 , 처리 

#다중행력  입력
datalist =(("이순신","010-222"),("박문수","010-567"))
cur.executemany("insert into PhoneBook Values(?,?);",datalist)

name = "chltjdgns"
phoneNum = "010-222"

cur.execute("insert into PhoneBook Values(?,?);",(name,phoneNum))
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print("{0},{1}".format(row,type(row)))

print("---fetch()---")
print(cur.fetchone())
print("----fetchmany---")
print(cur.fetchmany(2))
print("----fetchall----")
print(cur.fetchall())