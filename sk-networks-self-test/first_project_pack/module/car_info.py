from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class CarInfo:
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def fetch_top_cars(self, company):
        url = f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={company}+자동차"
        self.driver.get(url)

        # 조회수순으로 탭 클릭 대기
        try:
            sort_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-value='조회수순|'] a[href='#'] span.menu"))
            )
            print("조회수순 버튼이 존재합니다.")

            # 버튼 클릭을 위한 액션 체인 (스크롤을 내려서 버튼을 화면에 보이게 할 수도 있음)
            actions = ActionChains(self.driver)
            actions.move_to_element(sort_button).click().perform()
            print("조회수순 버튼 클릭 완료")

            # 자동차 정보가 로드될 때까지 기다리기
            self.driver.implicitly_wait(3)

            # 자동차 정보 가져오기
            car_elements = self.driver.find_elements(By.XPATH, "//div[@class='info_box']")
            cars = []
            for car in car_elements[:4]:  # 첫 4개의 자동차 정보만 가져오기
                try:
                    # 자동차 이름
                    name = car.find_element(By.XPATH, './/strong[@class="title"]/a').text

                    # 가격 정보 (여기서 가격이 두 개의 span 태그에 나뉘어 있는 경우를 고려)
                    price = car.find_element(By.XPATH, ".//div[@class='sub_info']/span[@class='info_txt']").text

                    # 연비 정보 (연비가 따로 나와 있을 경우)
                    mileage = car.find_element(By.XPATH, ".//div[@class='sub_info'][2]/span[@class='info_txt']").text

                    # 자동차 정보 딕셔너리로 저장
                    cars.append({
                        "name": name,
                        "price": price,
                        "mileage": mileage
                    })
                except Exception as e:
                    print(f"정보 추출 중 오류 발생: {e}")
                    continue
            return cars
        except Exception as e:
            print(f"클릭 안됨: {str(e)}")
            return []

    def close(self):
        self.driver.quit()
