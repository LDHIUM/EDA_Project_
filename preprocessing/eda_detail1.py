import pandas as pd

def convert_csv_values(input_file, output_file, column_name, value_mapping):
    # Load the CSV file
    df = pd.read_csv(input_file)
    
    # 칼럼에 딕셔너리 key를 value로 변경하는 과정
    df[column_name] = df[column_name].replace(value_mapping)
    
    # 새로운 CSV file로 저장
    df.to_csv(output_file, index=False, encoding='utf-8-sig')

detail_list = {
    'Ahmed ElMohamady': 'Ahmed El Mohamady',
    'Alex Oxlade-Chamberlain': 'Alex Oxlade Chamberlain',
    'Alisson': 'Alisson Becker',
    'Amad Diallo Traore': 'Amad Diallo',
    'Andrew Robertson': 'Andy Robertson',
    'Andriy Yarmolenko': 'Andrii Yarmolenko',
    'Armel Bella Kotchap': 'Armel Bella-Kotchap',
    'Arnaut Danjuma Groeneveld': 'Arnaut Danjuma',
    'Benoit Badiashile Mukinayi': 'Benoit Badiashile',
    'Bernardo': 'Bernardo Espinosa',
    'Bobby Reid': 'Bobby De Cordova-Reid',
    'Brad Jones': 'Bradley Jones',
    'Bryan Gil Salvatierra': 'Bryan Gil',
    'Cheick Oumar Doucoure': 'Cheick Doucoure',
    'Daniel Bentley': 'Dan Bentley',
    'Daniel Drinkwater': 'Danny Drinkwater',
    "Daniel N'Lundulu": 'Daniel Nlundulu',
    'Emile Smith-Rowe': 'Emile Smith Rowe',
    'Eric Maxim Choupo-Moting': 'Eric Choupo-Moting',
    'Estupinan': 'Pervis Estupinan',
    'Ezri Konsa Ngoyo': 'Ezri Konsa',
    'Facao': 'Radamel Falcao',
    'Faustino Anjorin': 'Tino Anjorin',
    'Fernando Marcal': 'Marcal',
    'Franck Zambo': 'Andre-Frank Zambo Anguissa',
    'Hamed Junior Traore': 'Hamed Traore',
    'Hee-Chan Hwang': 'Hwang Hee-Chan',
    'Ian Poveda-Ocampo': 'Ian Poveda',
    'Jaden Philogene-Bidace': 'Jaden Philogene',
    'Joe Ayodele-Aribo': 'Joe Aribo',
    "Joey O'Brien": "Joseph O'Brien",
    'Johann Berg Gudmundsson': 'Johann Gudmundsson',
    'Jonathan Williams': 'Jonny Williams',
    'Jonny': 'Jonny Otto',
    'Jose Angel Crespo': 'Jose Crespo',
    'Jose Pozo': 'Jose Angel Pozo',
    'Jose Reina': 'Pepe Reina',
    'Joseph Gomez': 'Joe Gomez',
    'Joseph Hodge': 'Joe Hodge',
    'Joseph Whitworth': 'Joe Whitworth',
    'Joshua Sargent': 'Josh Sargent',
    'Juan Camilo Hernandez': 'Cucho Hernandez',
    'Juan Zuniga': 'Juan Camilo Zuniga',
    'Jurado': 'Jose Manuel Jurado',
    'Ki Sung-yueng': 'Ki Sung-Yueng',
    'Konstantinos Tsimikas': 'Kostas Tsimikas',
    'Lasse Sorenson': 'Lasse Soerensen',
    'Lee Chung-yong': 'Lee Chung-Yong',
    'Leo Fuhr Hjelde': 'Leo Hjelde',
    'Mads Bech Soerensen': 'Mads Bech',
    'Mame Biram Diouf': 'Mame Diouf',
    'Martin Odegaard': 'Martin Oedegaard',
    'Mat Ryan': 'Mathew Ryan',
    'Matt Worthington': 'Matthew Worthington',
    'Matthew Cash': 'Matty Cash',
    'Matthew James': 'Matty James',
    'Matthew Longstaff': 'Matty Longstaff',
    'Max Gradel': 'Max-Alain Gradel',
    'Max Kilman': 'Maximilian Kilman',
    'Naif Aguerd': 'Nayef Aguerd',
    "Nicolas N'Koulou": 'Nicolas Nkoulou',
    'Nsue': 'Emilio Nsue',
    'Nyom': 'Allan-Romeo Nyom',
    'Oghenekaro Etebo': 'Peter Etebo',
    'Pape Sarr': 'Pape Matar Sarr',
    'Papiss Demba Cisse': 'Papiss Cisse',
    'Rayan Ait Nouri': 'Rayan Ait-Nouri',
    'Ritchie de Laet': 'Ritchie De Laet',
    'Robbie Brady': 'Robert Brady',
    'Santiago Cazorla': 'Santi Cazorla',
    'Sokratis': 'Sokratis Papastathopoulos',
    "Steven N'Zonzi": 'Steven Nzonzi',
    'Tanguy NDombele Alvaro': 'Tanguy Ndombele',
    'Toti': 'Toti Gomes',
    'Tyias Browning': 'Jiang Guangtai',
    'Valentino Livramento': 'Tino Livramento',
    'Vicente Iborra': 'Iborra',
    'William Smallbone': 'Will Smallbone'
}
# input and output 파일 경로
input_file_path = "C:/Users/LEGION/Downloads/EDA 프로젝트/understat_all.csv"
output_file_path = "C:/Users/LEGION/Downloads/EDA 프로젝트/understat_all0.csv"

convert_csv_values(input_file_path, output_file_path, "Player", detail_list)