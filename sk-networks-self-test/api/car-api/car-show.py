import csv
import pymysql
import pandas as pd
 
#DB 연결
conn = pymysql.connect(
    host = 'localhost',
    user = 'squirrel',
    password = 'squirrel',
    database = 'cardb'
)

cur = conn.cursor()

file_name = 'car-data-excel.xlsx'
df = pd.read_excel(file_name, header=[0, 1])

df = df.loc[:, ~df.columns.get_level_values(1).str.contains('계')]

# 엑셀 데이터 처리
for index, row in df.iterrows():
    
    # 월별 테이블에 해당 월 데이터가 있는지 확인
    cur.execute(
        'select monthly_id from car_monthly where month_year = %s',
        (row[0],)
    )
    monthly_result = cur.fetchone()
    if monthly_result is None:
        cur.execute(
            'insert into car_monthly (month_year) values (%s)',
            (row[0],)   
        )
        print('car_monthly insert 실행')
        #conn.commit()
        cur.execute('select last_insert_id()')
        # 아래서 카 데이터에 들어갈 예정
        monthly_id = cur.fetchone()[0]
    else:
        monthly_id = monthly_result[0]
    #conn.commit()
        
    # car_region 중복 확인
    cur.execute(
        'select region_id from car_region where sido_name = %s and sigungu_name = %s',
        (row[1], row[2])
    )
    region_result = cur.fetchone()
    if region_result is None:
        cur.execute(
            'insert into car_region (sido_name, sigungu_name) values (%s, %s)',
            (row[1], row[2])
        )
        #print('car_region insert 실행')
        # conn.commit()
        cur.execute('select last_insert_id()')
        region_id = cur.fetchone()[0]
    else:
        region_id = region_result[0]

    # 차량 데이터 삽입
    car_counts = row[3:15].values
    car_types = ['승용','승합','화물','특수']
        
    for i, count in enumerate(car_counts):
        # 계 건너뛰기기
        if isinstance(count, str) and '계' in count:
            continue
        # 천 단위 구분자 ',' 제거 후 숫자 형식으로 변환
        count = str(count).replace(",", "")  # 천 단위 구분자 제거
        
        # car_type 4번뒤 순회 예정
        cur.execute(
            'select type_id from car_type where type_name = %s',
            (car_types[i // 4],)
        )
        type_id = cur.fetchone()[0]
            
        # 1 2 3 순회마다 부여여
        race_id = (i%3) + 1
            
        cur.execute(
            'insert into car_data (region_id, monthly_id, type_id, race_id, vehicle_count) values (%s, %s, %s, %s, %s)',
            (region_id, monthly_id, type_id, race_id, count)
        )
            
            
    total_counts = row[15:18]
    for i, total in enumerate(total_counts):
        if isinstance(count, str) and '계' in count:
            continue
        total = str(total).replace(',','')
        race_id = (i%3) + 1
        cur.execute(
            'insert into car_total (region_id, monthly_id, race_id, total_count) values(%s, %s, %s, %s)',
            (region_id, monthly_id, race_id, total)
        )

conn.commit()
cur.close()
conn.close()