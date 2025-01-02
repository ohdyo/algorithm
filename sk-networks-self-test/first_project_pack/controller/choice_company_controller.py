from module.car_info import CarInfo
from view.page_ui import PageUI

class ChoiceCompanyController:
    def __init__(self):
        self.car_data = CarInfo()

    def run(self):
        brand = PageUI.display_options()
        if brand:
            results = self.car_data.fetch_top_cars(brand)
            PageUI.display_results(results)
