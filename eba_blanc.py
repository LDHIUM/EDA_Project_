import pandas as pd

special_characters = ['(on loan from )']

years_range = list(range(2014, 2023))


def blanc_edit(season):
    file_path = fr"C:\Users\LEGION\Downloads\EDA 프로젝트\1xbet_defensive_{season}_edited0.csv"
    defensive = pd.read_csv(file_path)

    # Translate the "Name" column
    for index, row in defensive.iterrows():
        name_blanc = row["Name"].replace(' ','')
        defensive.at[index, "Name"] = name_blanc
    # Save the translated DataFrame
    translated_file_path = fr"C:\Users\LEGION\Downloads\1xbet_defensive_{season}_edited1.csv"
    defensive.to_csv(translated_file_path, index=False, encoding='utf-8-sig')

# Call the rename function for each year in the years_range


blanc_edit(2022)
