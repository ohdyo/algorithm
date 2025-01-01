#설치 명령어 (이거 한줄만 치면 다 알아서 다운해줌)
# pip install selenium webdriver-manager pandas streamlit
import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Selenium으로 데이터를 크롤링하는 함수
#
def get_search_results():
    # 해당 코드는 위에서 임포트한 webdriver를 이용해서 크롬창을 열기위한 용도
    # 드라이버에 담아둔다.
    driver = webdriver.Chrome()

    try:
        # Google 홈페이지 열기
        # 크롬에서 무슨 창을 열것인지 드라이버에게 전달해준다.
        driver.get("https://www.google.com")

        # 검색창 찾기
        # 구글 검색창을 열고 'f12'버튼을 눌르면 개발자도구라고 웹사이트 창에 이상한 영어가 뜰것이다.
        # 우리는 이걸 html언어라 하는데 웹사이트의 화면을 구성해주는 코드이다.
        # 여기서 열린 개발자 도구의 좌측 상단을 보면 점선으로 이뤄진 사각형에 마우스커서가 겹쳐있는 보인다.
        # 이를 클릭하고 웹사이트창의 구글 검색칸에 커서를 가져다대면
        # 이상한 색깔로 변하면서 무슨 영어로 설명해주는 사각박스가 보인다.
        # 그게 보인다면 클릭해보고 클릭하게 되면 html파일이 해당 구역이 이 코드로 구성돼있다고 색깔이 변한걸 확인가능하다.
        # !! 여기서 제일 중요
        # 아래 이상한 영어가 클릭시 빛나는 부분인데 이걸 포함한 html코드를 전부 읽는건 자원적으로
        # 손해이기에 selenium은 이 중 하나만 읽어서 가져올려고 한다.
        # 그걸 선택해주는 요소는 개발자가 정할수 있다.
        # 지금의 경우 'By.Name'이라는 옵션을 인자로 사용했다.
        # 이러면 아래 영어에서 'name'이라는 키속성에서 'q'라 적혀있는것만 가져오겠다.
        # 라는 뜻이다
        # <textarea class="gLFyf" aria-controls="Alh6id" aria-owns="Alh6id" autofocus="" title="검색"
        # value="" jsaction="paste:puy29d;" aria-label="검색" placeholder=""
        # aria-autocomplete="both" aria-expanded="false" aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off"
        # id="APjFqb" maxlength="2048"
        # name="q" role="combobox" rows="1" spellcheck="false" data-ved="0ahUKEwjQx-Sv2dSKAxVZr1YBHeIoOC8Q39UDCA8"></textarea>
        search_box = driver.find_element(By.NAME, "q")
        # name 속성에 'q'라 적혀있는건 검색창 하나이기에 이걸
        # 파이썬의 search_box라는 변수에 담아둔다.

        # 검색어 입력
        # search_box에 해당 문자열을 보내게 해주는 역할을 하는 함수이다.
        search_box.send_keys("Python Selenium 예제")
        # 보내고 나서 엔터를 눌러주는 역할
        search_box.send_keys(Keys.RETURN)

        # 검색 결과 대기
        # 이건 실행하는데 오래걸릴수있고 나중에 비동기방식에 배우게 될테니
        # 그때 자세하게 설명 들으면 좋다.
        # 지금은 쉽게 실행하는데 좀 기달려 달라는 코드이다.
        time.sleep(2)

        # 검색 결과 가져오기
        # 넘어간 페이지에서 해당하는 태그의 값을 반환해준다.
        # 지금의 경우 CSS_SELECTOR가 인자로 사용됐는데 이것은
        # html페이지에서 가장 폭 넓게 사용하기 좋은 것으로
        # 뒤의 적힌 문자열 div.g에 해당하는 모든 값을 가져오게 해준다.
        # 지금의 경우 <div class = 'g'>에 해당하는 모든값 가져온다.
        results = driver.find_elements(By.CSS_SELECTOR, "div.g")


        # 결과 저장
        search_data = []
        for result in results[:5]:  # 상위 5개 결과만 사용
            title = result.find_element(By.TAG_NAME, "h3").text
            link = result.find_element(By.TAG_NAME, "a").get_attribute("href")
            search_data.append({"Title": title, "Link": link})

        return search_data
    finally:
        # 브라우저 닫기
        driver.quit()


# Streamlit 페이지 제목
st.title('Google 검색 결과')

# 검색 결과 가져오기
search_results = get_search_results()

# Pandas DataFrame으로 변환
df = pd.DataFrame(search_results)

# DataFrame을 Streamlit 페이지에 표시
st.dataframe(df)
