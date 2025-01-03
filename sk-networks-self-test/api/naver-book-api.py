import urllib.parse
import urllib.request
import urllib.response
import json

import mysql.connector


#api 호출을 위해서 발급받은 id와 secret key
client_id = 'icefiP59Jnm9GVBYJoIs'
client_secret = 'vRLgd8Vo1B'

#query뒤에 검색할 단어를 encoding
encText = urllib.parse.quote('한강')

# 요청 url 뒤에 검색어('query=' 뒤에)를 붙여줌
# 1. json 방식
url = 'https://openapi.naver.com/v1/search/blog.json?query=' + encText

request = urllib.request.Request(url)

request.add_header('X-Naver-Client-Id',client_id)
request.add_header('X-Naver-Client-Secret',client_secret)

response = urllib.request.urlopen(request)

# 여기까지 하면 api요청으로 데이터를 가져왔지만 내가 사용하는 방식으로는 데이터를 가져오지 못한 상태
results = response.read().decode('utf-8')

#print(type(results))

#내가 쓸수있는 데이터로 가공하기 위해 json파일로 형식을 리로드(=변환)해준다.
datas = json.loads(results)

#변환한 파일을 파이썬의 딕셔너리 함수에 담기위해 선언
result_dict = {}

# 딕셔너리 함수 내 리스트요소로 사용될 리스트들 선언
title = []
link = []
desc = []

# json형식을 보고 반복문 실행
# 가볍게 보면 {
#   '무슨 키1' : 데이터1
#   '무슨 키2' : 데이터2
#   'items' : {
#       'title' = 제목에 해당하는 데이터1
#        'link' = 링크에 해당하는 데이터1
#       'desc' = 묘사에 해당하는 데이터1
#       ...
#             },
#             {
#       'title' = 제목에 해당하는 데이터2
#        'link' = 링크에 해당하는 데이터2
#       'desc' = 묘사에 해당하는 데이터2
#       ...
#        }    
#}
# 이런 형식으로 담겼기에 반복문의 형식이 저렇게 작성한것이다.
# for data in datas['items']:
#     title.append(data['title'])
#     link.append(data['link'])
#     desc.append(data['description'])

result_dict = {
    'title' : title,
    'link' : link,
    'desc' : desc
}
book_list = datas['items']

# mysql connector
conn = mysql.connector.connect(
    host='localhost',
    user='squirrel',
    password='squirrel',
    database = 'bookdb'
)

cursor = conn.cursor()

sql = '''insert into book_info(book_title,book_image,book_author, 
                                book_publisher, book_isbn, 
                                book_description, book_pub_date) 
                        values(%s, %s, %s, %s, %s, %s, %s)'''

# 딕셔너리에 담을시 이렇게 반복으로 쿼리 실행 후 저장
# for i in range(10):
#     val = (result_dict['title'][i], result_dict['link'][i], result_dict['desc'][i])
#     cursor.execute(sql,val)
#     conn.commit()
print(book_list)
for book_info in book_list:
    values = (book_info['title'], book_info['image'], 
              book_info['author'], str(book_info['publisher']), 
              book_info['isbn'], book_info['description'], 
              book_info['pub_date'])
    cursor.execute(sql,values)
    
conn.commit()
    
cursor.close()
conn.close()