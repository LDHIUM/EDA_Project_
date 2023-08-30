import pandas as pd

def convert_csv_values(input_file, output_file, column_name, value_mapping):
    # Load the CSV file
    df = pd.read_csv(input_file)
    
    # Apply value mapping to the specified column
    df[column_name] = df[column_name].replace(value_mapping)
    
    # Save the transformed DataFrame to a new CSV file
    df.to_csv(output_file, index=False, encoding='utf-8-sig')


detail_list = {
    'David De Gea': 'David de Gea',
    'Virgil Van Dijk': 'Virgil van Dijk',
    'Rodrigo Hernandez Cascante': 'Rodri',
    'Daniel Bentley': 'Dan Bentley',
    'Carlos Casimiro': 'Casemiro',
    'Kepa Arrizabalaga': 'Kepa',
    'Fabinho Tavares': 'Fabinho',
    'Antony dos Santo': 'Antony',
    'Frederico de Paula Santos': 'Fred',
    'Jorge Luiz Frello Filho': 'Jorginho',
    'Edward Nketiah': 'Eddie Nketiah',
    'David Fofana': 'David Datro Fofana',
    'Rodrigo Machado': 'Rodrigo',
    'Andrew Robertson': 'Andy Robertson',
    'Ederson Moraes': 'Ederson',
    'Jose Moutinho': 'Joao Moutinho',
    'Emerson Palmieri': 'Emerson',
    'Richarlison de Andrade': 'Richarlison',
    'Joelinton Cassio Apolinario de Lira': 'Joelinton',
    'Felipe Augusto de Almeida': 'Felipe',
    'Onyinye Ndidi': 'Wilfred Ndidi',
    'Pape Sarr': 'Pape Matar Sarr',
    'Pierre-Emile Hojbjerg': 'Pierre-Emile Hoejbjerg',
    'Heung-Min Son': 'Son Heung-Min',
    'Alex Oxlade-Chamberlain': 'Alex Oxlade Chamberlain',
    'Jared Bowen': 'Jarrod Bowen',
    'Vitaliy Mykolenko': 'Vitalii Mykolenko'
                }
# Specify input and output file paths
input_file_path = "C:/Users/LEGION/Downloads/EDA 프로젝트/salary_all.csv"
output_file_path = "C:/Users/LEGION/Downloads/EDA 프로젝트/salary_all0.csv"

# Call the function to convert values and save the result
convert_csv_values(input_file_path, output_file_path, "Name", detail_list)