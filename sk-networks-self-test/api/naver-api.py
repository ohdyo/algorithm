import urllib.parse
import urllib.request
import urllib.response

#api 호출을 위해서 발급받은 id와 secret key
client_id = 'icefiP59Jnm9GVBYJoIs'
client_secret = 'vRLgd8Vo1B'

#query뒤에 검색할 단어를 encoding
encText = urllib.parse.quote('오늘 점심')

# 요청 url 뒤에 검색어('query=' 뒤에에)를 붙여줌
# 1. json 방식
url = 'https://openapi.naver.com/v1/search/blog.json?query=' + encText
# 2. xml 방식
# url = 'https://openapi.naver.com/v1/search/blog.xml?query=' + encText

# 완성된 url을 요청하기위해 변수 request에 담아줌(객체 생성성)
# url형식으로 요청하게 해주는 방식이다.
request = urllib.request.Request(url)

# 객체로 생성된 변수에 헤더를 담아주는 곳곳
# 요청은 헤더 - 바디 부분으로 나누며 헤더에는 보통 인증에 필요한 데이터를 담는다.
# 아래는 이런 인증을 위한 데이터를 헤더에 담는 함수이다.
request.add_header('X-Naver-client-Id', client_id)
request.add_header('X-Naver-Client-Secret', client_secret)

# 응답을 반환받게 하기위해 response변수에 담아줌
# 요청url에 대한 응답을 urlopen함수를 통해 열어서 데이터를 받아옴
response = urllib.request.urlopen(request)

# response.getcode() -> 응답코드를 반환해주는 함수 200 = 정상통신 , 400 이상 = 개발자에 의한 에러

print(response.getcode())

# 응답 받은 데이터를 읽어오기 위해 response.read().decode('utf-8')을 통해서 데이터를 반환받을수 있음
response_body = response.read()
print(response_body.decode('utf-8'))
