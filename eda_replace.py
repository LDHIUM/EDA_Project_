import pandas as pd

# Weekly Salary_
# 1xbet_defensive_
# 1xbet_offensive_
# understat_

years_range = list(range(2014, 2023))

def replace_edit(season):
    file_path = fr"C:\Users\LEGION\Downloads\Weekly Salary_edited{season}.csv"
    defensive = pd.read_csv(file_path)

    # Translate the "Name" column
    for index, row in defensive.iterrows():
        name_replace = row["Name"].replace('(on loan from )','')
        defensive.at[index, "Name"] = name_replace
    # Save the translated DataFrame
    translated_file_path = fr"C:\Users\LEGION\Downloads\Weekly Salary_{season}_edited0.csv"
    defensive.to_csv(translated_file_path, index=False, encoding='utf-8-sig')

# Call the rename function for each year in the years_range


for year in years_range:
    replace_edit(year)
