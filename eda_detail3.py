import pandas as pd

def no_convert(num,nam):
    # Read the CSV file
    csv_path = 'C:/Users/LEGION/Downloads/understat_all.csv'
    df = pd.read_csv(csv_path)

    for i in range(0,len(df[df['No'] == num])):
        # Find the row with 'No' column value of 
        row_index = df[df['No'] == num].index[i]

        # Update the 'Name' column value
        new_name = nam
        df.at[row_index, 'Player'] = new_name

    # Save the modified DataFrame to a new CSV file
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')

    print(df[df['No'] == num])

no_list = {493:'Gabriel Paulista',5613:'Gabriel Magalhaes',7430:'Emerson Royal',}

for key, value in no_list.items():
    no_convert(key,value)



