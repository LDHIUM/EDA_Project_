import pandas as pd

def convert_csv_values(input_file, output_file, column_name, value_mapping):
    # Load the CSV file
    df = pd.read_csv(input_file)
    
    # 칼럼에 딕셔너리 key를 value로 변경하는 과정
    df[column_name] = df[column_name].replace(value_mapping)
    
    # 새로운 CSV file로 저장
    df.to_csv(output_file, index=False, encoding='utf-8-sig')

detail_list =  {'Ahmed Elmohamady': 'Ahmed El Mohamady',
                'Alex Oxlade-Chamberlain': 'Alex Oxlade Chamberlain',
                'Alex Song': 'Alexandre Song',
                'Robbie Brady': 'Robert Brady',
                'Cheik Tiote': 'Cheick Tiote',
                'Andrew Robertson': 'Andy Robertson',
                "Joey O'Brien": "Joseph O'Brien",
                'Rob Green': 'Robert Green',
                'Papiss Demba Cisse': 'Papiss Cisse',
                'Falcao': 'Radamel Falcao',
                'Matthew Upson': 'Matt Upson',
                'Jonathan Williams': 'Jonny Williams',
                'John Mikel Obi': 'John Obi Mikel',
                'Rob Elliot': 'Robert Elliot',
                'Will Buckley': 'William Buckley',
                'Brad Jones': 'Bradley Jones',
                'Tyias Browning': 'Jiang Guangtai',
                'Danny Lafferty': 'Daniel Lafferty',
                'Jose Pozo': 'Jose Angel Pozo',
                'Izzy Brown': 'Isaiah Brown',
                'Zeki Fryers': 'Ezekiel Fryers',
                'Alexander Sorloth': 'Alexander Soerloth',
                'Alisson': 'Alisson Becker',
                'Allan Nyom': 'Allan-Romeo Nyom',
                'Andre Zambo Anguissa': 'Andre-Frank Zambo Anguissa',
                'Bobby Reid': 'Bobby De Cordova-Reid',
                'Kell Watts': 'Kelland Watts',
                'Charly Musonda Jr': 'Charly Musonda',
                'Christian Norgaard': 'Christian Noergaard',
                'Daniel Bentley': 'Dan Bentley',
                'Dan Agyei': 'Daniel Agyei',
                "Dan N'Lundulu": 'Daniel Nlundulu',
                'Dimitrios Giannoulis': 'Dimitris Giannoulis',
                'Eric Maxim Choupo-Moting': 'Eric Choupo-Moting',
                'Fin Stevens': 'Finley Stevens',
                "Georges-Kevin N'Koudou": "Georges-Kevin Nkoudou",
                'Hamed Junior Traore': 'Hamed Traore',
                'Vicente Iborra': 'Iborra',
                'Ilya Zabarnyi': 'Illia Zabarnyi',
                'Jacob Lungi Sorensen': 'Jacob Soerensen',
                'Joao Carlos Teixeira': 'Joao Teixeira',
                'Johann Berg Gudmundsson': 'Johann Gudmundsson',
                'Jon Gorenc-Stankovic': 'Jon Gorenc Stankovic',
                'Jonathan Howson': 'Jonny Howson',
                'Joe Dodoo': 'Joseph Dodoo',
                'Jota Peleteiro': 'Jota',
                'Camilo Zuniga': 'Juan Camilo Zuniga',
                'Kepa Arrizabalaga': 'Kepa',
                'Konstantinos Tsimikas': 'Kostas Tsimikas',
                'Lasse Sorensen': 'Lasse Soerensen',
                'Leo Fuhr Hjelde': 'Leo Hjelde',
                'Mads Bech Sorensen': 'Mads Bech',
                'Mads Roerslev Rasmussen': 'Mads Roerslev',
                'Martin Odegaard': 'Martin Oedegaard',
                'Matt Worthington': 'Matthew Worthington',
                'Matthew Longstaff': 'Matty Longstaff',
                'Max Gradel': 'Max-Alain Gradel',
                'Max Kilman': 'Maximilian Kilman',
                "Nicolas N'Koulou": 'Nicolas Nkoulou',
                'Orjan Nyland': 'Oerjan Nyland',
                'Pape Sarr': 'Pape Matar Sarr',
                'Oghenekaro Etebo': 'Peter Etebo',
                'Pierre-Emile Hojbjerg': 'Pierre-Emile Hoejbjerg',
                'Stefan Ortega Moreno': 'Stefan Ortega',
                'Khanya Leshabela': 'Thakgalo Leshabela',
                'Thiago': 'Thiago Alcantara',
                'Tom Edwards': 'Thomas Edwards',
                'Tommy Robson': 'Thomas Robson',
                'Vitaliy Mykolenko': 'Vitalii Mykolenko',
                'Bojan Krkic':'Bojan',
                'Hee-chan Hwang': 'Hwang Hee-Chan',
                'Chung-yong Lee': 'Lee Chung-Yong',
                'Sung-yong Ki': 'Ki Sung-Yueng',
                'Heung-min Son': 'Son Heung-Min',
                'Seok-yeong Yun':'Yun Suk-Young'}
    # input and output 파일 경로
input_file_path = "C:/Users/LEGION/Downloads/capology_all.csv"
output_file_path = "C:/Users/LEGION/Downloads/capology_all0.csv"

convert_csv_values(input_file_path, output_file_path, "Name", detail_list)