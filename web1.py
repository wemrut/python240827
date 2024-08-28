# web1.py

from bs4 import BeautifulSoup

page = open("Chap09_test.html","rt",encoding="utf-8").read()

#

soup = BeautifulSoup(page,"html.parser")

#전체보기

#rint(soup.prettify())
#print(soup.find_all("p"))

#조건문 : < class="outer-text">
#파이썬의 키워드와 충돌 class -> class_ 로 써야함
#attributes -> attrs
#print(soup.find_all("p",class_="outer-text"))

#print(soup.find_all("p",attrs={"class":"outer-text"}))

for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n","")
    print(title)


