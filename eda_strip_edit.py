import pandas as pd




years_range = list(range(2014, 2023))


def strip_edit(season):
    file_path = fr"C:\Users\LEGION\Downloads\Weekly Salary_{season}_edited0.csv"
    defensive = pd.read_csv(file_path)

    # Translate the "Name" column
    for index, row in defensive.iterrows():
        name_strip = row["Name"].strip()
        defensive.at[index, "Name"] = name_strip
    # Save the translated DataFrame
    translated_file_path = fr"C:\Users\LEGION\Downloads\Weekly Salary_{season}_edited.csv"
    defensive.to_csv(translated_file_path, index=False, encoding='utf-8-sig')

# Call the rename function for each year in the years_range


for year in years_range:
    strip_edit(year)




