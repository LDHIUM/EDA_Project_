import pandas as pd

special_characters = {
            'À': 'A',
            'Á': 'A',
            'Â': 'A',
            'Ã': 'A',
            'Ä': 'A',
            'Å': 'A',
            'Æ': 'Ae',
            'Ç': 'C',
            'È': 'E',
            'É': 'E',
            'Ê': 'E',
            'Ë': 'E',
            'Ì': 'I',
            'Í': 'I',
            'Î': 'I',
            'Ï': 'I',
            'Ð': 'D',
            'Ñ': 'N',
            'Ò': 'O',
            'Ó': 'O',
            'Ô': 'O',
            'Õ': 'O',
            'Ö': 'O',
            'Ø': 'O',
            'Ù': 'U',
            'Ú': 'U',
            'Û': 'U',
            'Ü': 'U',
            'Ý': 'Y',
            'Þ': 'Th',
            'ß': 'ss',
            'à': 'a',
            'á': 'a',
            'â': 'a',
            'ã': 'a',
            'ä': 'a',
            'å': 'a',
            'æ': 'ae',
            'ç': 'c',
            'è': 'e',
            'é': 'e',
            'ê': 'e',
            'ë': 'e',
            'ì': 'i',
            'í': 'i',
            'î': 'i',
            'ï': 'i',
            'ð': 'd',
            'ñ': 'n',
            'ò': 'o',
            'ó': 'o',
            'ô': 'o',
            'õ': 'o',
            'ö': 'o',
            'ø': 'o',
            'ù': 'u',
            'ú': 'u',
            'û': 'u',
            'ü': 'u',
            'ý': 'y',
            'þ': 'th',
            'ÿ': 'y',
            'Ć': 'C',
            'ć': 'c',
            'Č': 'C',
            'č': 'c',
            'Đ': 'Dj',
            'đ': 'dj',
            'Ğ': 'G',
            'ğ': 'g',
            'İ': 'I',
            'ı': 'i',
            'Ş': 'S',
            'ş': 's',
            'Š': 'S',
            'š': 's',
            'Ÿ': 'Y',
            'Ž': 'Z',
            'ž': 'z',
                }

def trans_and_convert(name):
    english_alphabet_name = ''.join([special_characters[char] if char in special_characters else char for char in name])
    return english_alphabet_name

# Weekly Salary_
# 1xbet_defensive_
# 1xbet_offensive_
# understat_

years_range = list(range(2014, 2023))

def alphbet_convert(season):
    file_path = fr"C:\Users\LEGION\Downloads\EDA 프로젝트\1차 자료\1xbet_offensive\1xbet_offensive_{season}.csv"
    file_name = pd.read_csv(file_path)

    # 딕셔너리로 정리해 놓은 수많은 언어의 알파벳이 발견되면 영어 알파벳으로 교체됩니다.
    for index, row in file_name.iterrows():
        name_en = trans_and_convert(row["Name"])
        file_name.at[index, "Name"] = name_en
    # 데이터를 다른 이름으로 다시 저장해 줍니다.
    translated_file_path = fr"C:\Users\LEGION\Downloads\1xbet_offensive_{season}_edited.csv"
    file_name.to_csv(translated_file_path, index=False, encoding='utf-8-sig')

# 딕셔너리 범위로 for문을 돌려줍니다.

for year in years_range:
    alphbet_convert(year)

