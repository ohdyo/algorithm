# model/car_data_model.py
import pymysql
import pandas as pd

class CarDataModel:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'squirrel'
        self.password = 'squirrel'
        self.database = 'cardb'
        self.conn = None

    def connect(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=3306
            )
            print("MySQL 연결 성공")
        except Exception as e:
            print(f"MySQL 연결 실패: {e}")

    def execute_query(self, query, params=None):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except Exception as e:
            print(f"쿼리 실행 실패: {e}")
            return None

    def execute_insert(self, query, params=None):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query, params)
                self.conn.commit()
        except Exception as e:
            print(f"삽입 실패: {e}")

    def close(self):
        if self.conn:
            self.conn.close()
            print("MySQL 연결 종료")

    def process_excel_data(self, file_name):
        df = pd.read_excel(file_name, header=[0, 1], skiprows=4)

        df = df.loc[:, ~df.columns.get_level_values(1).str.contains('계')]
        df = df.loc[:, ~df.columns.get_level_values(0).str.contains('총계')]
        df = df.loc[df['시군구'].values != '계']

        for index, row in df.iterrows():
            monthly_id = self.insert_monthly_data(row[0])
            region_id = self.insert_region_data(row[1], row[2])

            car_counts = row[3:].values
            car_types = ['승용', '승합', '화물', '특수']
            race_types = ['관용', '자가용', '영업용']

            for i, count in enumerate(car_counts):
                if pd.isna(count):
                    continue
                count = int(str(count).replace(",", ""))

                car_type_idx = i // len(race_types)
                race_type_idx = i % len(race_types)

                car_type = car_types[car_type_idx]
                race_type = race_types[race_type_idx]

                type_id = self.get_type_id(car_type)
                race_id = self.get_race_id(race_type)

                if type_id and race_id:
                    self.insert_car_data(region_id, monthly_id, type_id, race_id, count)

    def insert_monthly_data(self, month_year):
        query = "select monthly_id from car_monthly where month_year = %s"
        result = self.execute_query(query, (month_year,))
        if result is None:
            query = "insert into car_monthly (month_year) values (%s)"
            self.execute_insert(query, (month_year,))
            query = "select last_insert_id()"
            result = self.execute_query(query)
        return result[0] if result else None

    def insert_region_data(self, sido_name, sigungu_name):
        if not sido_name or not sigungu_name:
            print(f"Skipping region with empty values: {sido_name}, {sigungu_name}")
            return None  # 값을 건너뛰기
        
        print(f"Checking region: {sido_name}, {sigungu_name}")  # 디버깅용
        query = "select region_id from car_region where sido_name = %s and sigungu_name = %s"
        result = self.execute_query(query, (sido_name, sigungu_name))
        
        if result is None:
            print(f"Region not found, inserting: {sido_name}, {sigungu_name}")  # 디버깅용
            query = "insert into car_region (sido_name, sigungu_name) values (%s, %s)"
            self.execute_insert(query, (sido_name, sigungu_name))
            
            # 커넥션을 통해 last_insert_id() 호출
            query = "select last_insert_id()"
            result = self.execute_query(query)  # 삽입 직후 last_insert_id() 호출
            
            if result:
                print(f"Inserted region_id: {result[0]}")  # 디버깅용
            
        return result[0] if result else None

    def insert_car_data(self, region_id, monthly_id, type_id, race_id, count):
        query = '''
            insert into car_data (region_id, monthly_id, type_id, race_id, vehicle_count)
            values (%s, %s, %s, %s, %s)
        '''
        self.execute_insert(query, (region_id, monthly_id, type_id, race_id, count))

    def get_type_id(self, car_type):
        query = "select type_id from car_type where type_name = %s"
        result = self.execute_query(query, (car_type,))
        return result[0][0] if result else None

    def get_race_id(self, race_type):
        query = "select race_id from race_type where race_name = %s"
        result = self.execute_query(query, (race_type,))
        return result[0][0] if result else None
