# controller/car_data_controller.py
from model.car_data_model import CarDataModel

class CarDataController:
    def __init__(self):
        self.model = CarDataModel()

    def run(self, file_name):
        self.model.connect()  # DB 연결
        self.model.process_excel_data(file_name)  # 엑셀 데이터 처리
        self.model.close()  # DB 연결 종료
