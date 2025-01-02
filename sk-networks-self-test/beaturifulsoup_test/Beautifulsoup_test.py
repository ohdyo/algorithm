# 실행 전 cmd창에서 해당 명령어 실행
# 1. pip install pymysql
# 2. pip install beautifulsoup4 
# 3. pip install streamlit
# 4. pip install pandas


# -- 여기는 해당 메서드와 함수를 실행시키기위한 라이브러리 임포트 부분

#API Request
import requests
from urllib import request
#beautifulsoup
from bs4 import BeautifulSoup

#streamlit & pandas
import streamlit as st
import pandas as pd

#seleniunm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# -- 여기까지 임포트 부분분

# -- python db 연동

#mysql connector
import pymysql

#-- mysql
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='squirrel',
    passwd='squirrel',
    db='menudb',
    charset='utf8'
)

# 연결한 DB의 커서역할하는 변수 , 커서에 sql문을 삽입하는 방식으로 사용 
cur = conn.cursor()
print(cur.connection.db)
sql = 'select * from tbl_menu'

#커서에 sql 삽입해서 실행
cur.execute(sql)
print(f'cur.rowcount = {cur.rowcount}')

# sql 실행시키고 나온 튜플들을 변수 rows에 담음 
# 그래서 row의 자료형(마우스 갖다대면 보임)은 tuple형식으로 변함
rows = cur.fetchall()
if not rows:
    print('없음')
else :
    print(rows)

# 현재 귀차니즘의 관계로 데이터를 추가,삭제는 구현 안함
# 결과 값이 프린트 구문으로 나와요
# 원래는 딕셔너리 함수로 streamlit으로 보여줄려 했는데 귀차니즘... ㅎ
# -- 파이썬 db끝


#-- selenium (아직 진행중, 미완성)
# driver = webdriver.Chrome()
# driver.get('https://www.google.co.kr/')
# time.sleep(3)

#search_box = driver.find_element(By.CLASS_NAME, 'gLFyf.gsfi')
#search_box = driver.find_element_by_xpath('//*[@id="google_search"]')

# -- selenium 끝

#-- beautifulsoup
# 해당 url 클릭하면 이상한 문자 나오는데 html문이라고 
# 나중에 강사님이 알려줄테니 그냥 화면을 구성하는 요소들을 글자화 시킨거라 생각해는게 편함
target = request.urlopen('http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108')

# url을 변수 soup에 담음, target은 위에서 선언한 변수고 이를 html페이지로 변환해서 담음
soup = BeautifulSoup(target, 'html.parser')


city = []
wf = []
tmn = []
tmx = []

# html에서 <body>의 요소 중 <location>을 기준으로 그 안쪽의 city,wf,tmn,tmx의 데이터를 미리 선언한 배열에 삽입함
# html 페이지를 보면 중간에 <body> 태그 적혀있고
# 그 아래 tab으로 한칸 띄어서 city wf tmn tmx 다 있음
for location in soup.select('location'):
    city.append(location.select_one('city').string)
    wf.append(location.select_one('wf').string)
    tmn.append(location.select_one('tmn').string)
    tmx.append(location.select_one('tmx').string)

# 데이터가 추가된 배열들을
# 내가 선언한 딕셔너리 함수(weather_dict)에 key값에 맞춰서 삽입입
weather_dict = {
    'city' : city,
    'wf' : wf,
    'tmn' : tmn,
    'tmx' : tmx
}

# pandas를 통해 데이터를 구조화
data = pd.DataFrame(weather_dict)

#구조화한 데이터를 streamlit에서 시각적으로 보이게 만듬듬
st.dataframe(data, use_container_width=True)

# -- beautifulsoup 끝끝

# 공공데이터 포탈(or 다른 사이트에서 받은 API 데이터 가져오기)
# 반.드.시 url에 적혀있는 /로 구분짓은 곳 이해하기
# 1. https : 일단 넘어가세요 통신 방식입니다.
# 2. api.odcloud.kr 여기가 이 데이터를 주는 곳입니다. (집 역할)
# 3. api : api통신 하기 전에 붙이는 단어 여기 뒤부터 중요
# 4. 3048950~/~~/~~ae9f7d23b2ea : 집에서 데이터가 있는 방을 찾아주는 곳 이건 암호화된거라 이해하지마세요
# 5. servicekey : 보통 데이터는 인증키를 발급받아서 servicekey뒤에 받아야 사용 가능
# 5-1 : 해당 부분은 개인 발급키로 방을 들어가기 위한 열쇠라 생각하면 편함 보안처리된 문자라 key 뒤에 별 뜻은 없음
url = 'https://api.odcloud.kr/api/3048950/v1/uddi:cfacb574-690a-4544-b750-ae9f7d23b2ea?page=2&perPage=10&serviceKey=XusVOv2JX0U1cpinxbbIXDfbWLJ5%2F1e8yLb89ChoUTFAD%2F%2BRKqd7rxb1fc23o4gXjF65JXYd%2BK4f0hPin2E0UA%3D%3D'
params = {
    
}

# requests : 간단하게 '요청한다'라 생각하는게 편한ㅁ
#           요청을 url(=위에 적힌 주소)에 보내서 해당 url과 키가 맞으면
#           사이트에서 지정한 data를 반환해준다.
response = requests.get(url)

# json : 데이터가 담겨서 오는 형식을 말함
# json은 파이썬의 딕셔너리함수와 흡사한 형태
# key와 값으로 이뤄져있어 파이썬에서도 보통 딕셔너리 함수에 값을 저장한다.
datas = response.json()

# 아래 주석 풀면 cmd창에서 데이터 확인 가능
# print(datas)

recall_date = []
recall_reason = []
made_company = []

for data in datas['data']:
    recall_date.append(data['리콜개시일'])
    recall_reason.append(data['리콜사유'])
    made_company.append(data['제작사'])
    
car_dict = {
    '리콜개시일' : recall_date,
    '리콜사유' : recall_reason,
    '제작사' : made_company
}

other_data = pd.DataFrame(car_dict)
st.dataframe(other_data, use_container_width=True)