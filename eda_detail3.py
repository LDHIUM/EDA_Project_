import pandas as pd

def no_convert(num,nam):
    # CSV파일 읽기
    csv_path = 'C:/Users/LEGION/Downloads/understat_all.csv'
    df = pd.read_csv(csv_path)

    for i in range(0,len(df[df['No'] == num])):
        # 'No'칼럼에서 원하는 번호 찾기
        row_index = df[df['No'] == num].index[i]

        # 새로운 값으로 바꿔주기
        new_name = nam
        df.at[row_index, 'Player'] = new_name

    # CSV 파일 수정해서 위에 덮어쓰기
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')

    print(df[df['No'] == num])

no_list = {493:'Gabriel Paulista',5613:'Gabriel Magalhaes',7430:'Emerson Royal',}

for key, value in no_list.items():
    no_convert(key,value)



