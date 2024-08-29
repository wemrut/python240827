#DemoForm2.py
#DemoForm2.UI(화면단)+ DemoForm2.py(로직단)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#웹서버와 통신
import requests
#웹크롤링
from bs4 import BeautifulSoup

#디자인파일 로딩
#파일명 변경
form_class = uic.loadUiType("DemoForm2.ui")[0]

#윈도우 클래스 정의(QMainWindow)
class DemoForm(QMainWindow,form_class): # 상속받는 클래스 변경
    #초기화 로딩
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.label.setText("첫번째 화면 출력")
    #슬롯메서드
    def firstClick(self):

        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)

        #검색을 할  soup객체 생성
        soup = BeautifulSoup(response.text , "html.parser")
        #파일로 저장
        f= open("dangn.txt","wt",encoding="utf-8")
        posts = soup.find_all("div", attrs={"class":"card-desc"})

        for post in posts:
            titleElem = post.find("h2",attrs={"class":"card-title"})
            priceElem = post.find("div",attrs={"class":"card-price"})
            addrElem  = post.find("div",attrs={"class":"card-region-name"})
            #문자열만 추출
            title = titleElem.text.strip()
            price = priceElem.text.strip()
            addr = addrElem.text.strip()

            print(f"{title},{price},{addr}")
            f.write(f"{title},{price},{addr}\n")
        f.close()
        self.label.setText("당근마켓 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼클릭")

#작업 모듈을 실행되는지를 체크 (진입점 체크)
        
if __name__  =="__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()

    