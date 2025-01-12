# main.py
from controller.car_data_controller import CarDataController

def main():
    file_name = 'C:/Users/ljh10/Downloads/자동차등록현황보고_자동차등록대수현황 시도별 (201101 ~ 202412).xlsx'
    controller = CarDataController()
    controller.run(file_name)

if __name__ == "__main__":
    main()
