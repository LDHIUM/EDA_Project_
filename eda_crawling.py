import requests
import json
import csv
# 각 시즌별로 비패턴 코드로 되어 있어서 딕셔너리고 정리를 했습니다.
season = {2022:20934,2021:19793,2020:18685,2019:17590,2018:16368,2017:15151,2016:13796,2015:12496,2014:9155}

def crawl_defensive(season,num):
    url = f"https://1xbet.whoscored.com/StatisticsFeed/1/GetPlayerStatistics?category=summary&subcategory=defensive&statsAccumulationType=0&isCurrent=true&playerId=&teamIds=&matchId=&stageId={season}&tournamentOptions=2&sortBy=Rating&sortAscending=&age=&ageComparisonType=&appearances=&appearancesComparisonType=&field=Overall&nationality=&positionOptions=&timeOfTheGameEnd=&timeOfTheGameStart=&isMinApp=false&page=&includeZeroValues=&numberOfPlayersToPick=600"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)
    player_stats = json_data["playerTableStats"]
    result_list = [['Name','Team','Age','Position','Apps','Mins','Tackles','Inter','Fouls','Offsides','Clear','Drb','Blocks','Rating']]
    for player_stat in player_stats:
        name = player_stat['name']
        team = player_stat['teamName']
        age = player_stat['age']
        position = player_stat['positionText']
        apps = player_stat['apps']
        min = player_stat['minsPlayed']
        tackles = player_stat['tacklePerGame']
        inter = player_stat['interceptionPerGame']
        fouls = player_stat['foulsPerGame']
        offsides = player_stat['offsideWonPerGame']
        clear = player_stat['clearancePerGame']
        drb = player_stat['wasDribbledPerGame']
        blocks = player_stat['outfielderBlockPerGame']
        rating = player_stat['rating']
        result_list.append([name,team,age,position,apps,min,tackles,inter,fouls,offsides,clear,drb,blocks,rating])

    with open(f'1xbet_defensive_{num}.csv', 'a', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(result_list)
   
for i in season.keys():
    crawl_defensive(season[i],i)


