# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):

        try:                       
                #클리앙의 중고장터 주소 
                data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
                #웹브라우져 헤더 추가 
                print(data)
                req = urllib.request.Request(data,headers = hdr) # 웹브라우저인냥 행세
                data = urllib.request.urlopen(req).read()
                #한글이 깨지면 디코딩
                page = data.decode('utf-8', 'ignore')
                soup = BeautifulSoup(page, 'html.parser')
                list = soup.find_all('span', attrs={'data-role':'list-title-text'}) # key , value 로 가져옴


                # <span class="subject_fixed" data-role="list-title-text" title="아이패드 에어 (신형 M2) 13인치 256기가 팝니다.">
                #						아이패드 에어 (신형 M2) 13인치 256기가 팝니다.
                #					</span>
                for item in list:
                        try:
                                #<a class='list_subject'><span>text</span><span>text</span>
                                # span = item.contents[1]
                                # span2 = span.nextSibling.nextSibling
                                # title = span2.text 
                                title = item.text.strip()
                                #print(title)
                                if (re.search('아이폰', title)):
                                         print(title.strip())
                                         print('https://www.clien.net'  + item['href'])
                        except:
                                pass
        
        except:
                pass
        
