#web2.py
#웹서버와 통신
import requests
#웹크롤링
from bs4 import BeautifulSoup

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

# <div class="card-desc">
#       <h2 class="card-title">쌀</h2>
#       <div class="card-price ">
#         17,000원
#       </div>
#       <div class="card-region-name">
#         울산 북구 연암동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 17
#           </span>
#         ∙
#         <span>
#             채팅 17
#           </span>
#       </div>
#     </div>