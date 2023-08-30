import pandas as pd

# Weekly Salary_
# 1xbet_defensive_
# 1xbet_offensive_
# understat_

years_range = list(range(2014, 2023))

def strip_edit(season):
    file_path = fr"C:\Users\LEGION\Downloads\Weekly Salary_{season}_edited0.csv"
    defensive = pd.read_csv(file_path)

    # "Name" 칼럼 대체시키기
    for index, row in defensive.iterrows():
        name_strip = row["Name"].strip()
        defensive.at[index, "Name"] = name_strip
    # 데이터 다른이름으로 저장하기
    translated_file_path = fr"C:\Users\LEGION\Downloads\Weekly Salary_{season}_edited.csv"
    defensive.to_csv(translated_file_path, index=False, encoding='utf-8-sig')

# 리스트로 저장된 범위의 년도별로 for문 돌려주기

for year in years_range:
    strip_edit(year)




