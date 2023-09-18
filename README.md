# EDA_Project
- 팀명 : EDA_Champions 
- 주제 : Sports EDA(EPL) 
- 과정 : 자료수집-전처리-분석 
- 자료 : 2014/15-2022/23시즌 영국 프리미어리그 선수연봉 + 선수스탯 정보  
- 분석 : 40개가 넘는 피처들 간 비교 그래프를 통해 상관관계 분석
## Prerequisites
- BeautifulSoup
- Selenium
- requests
- matplotlib
- seaborn
- pandas
- numpy
- csv
- json
## Installation
```python
pip install <라이브러리>
```
## Features
- Apps : 총 출전 횟수
- Mins : 총 출전 시간(분)
- Rating : 시즌 평점
- SpG : 경기당 슈팅 횟수
- KeyP : 경기당 키패스 횟수
- Fouled : 경기당 파울 당한 횟수
- Off : 경기당 오프사이드에 걸린 횟수
- Disp : 경기당 드리블 실수로 (공 소유권 잃음)
- Drb_Off : 경기당 드리블 성공 횟수(공격지표)
- Drb_Def : 경기당 드리블을 당한 횟수(수비지표)
- UnsTch : 공 컨트롤 실수로 (공 소유권 잃음)
- Tackles : 경기당 태클 수
- Inter : 경기당 가로채기 수
- Fouls : 경기당 파울 한 횟수
- Offsides : 경기당 오프사이드 트랩 성공 횟수
- Clear : 경기당 공을 걷어 낸 횟수
- Blocks : 경기당 가로막은 횟수
- G : 한 시즌의 총 득점 수
- A : 한 시즌의 총 도움 수
- xG : 기대 득점 값(전 시즌 기준으로 계산 됨)
- xA : 기대 도움 값(전 시즌 기준으로 계산 됨)	
- AvgP : 경기당 패스 횟수
- PS% : 패스 성공률
- NPG : 페널티킥 없는 득점 수
- NPxG : 패널티킥 없는 기대 득점 값
- xG Chain : 슈팅까지 연결된 체인에 관여한 모든 선수에게 주는 기댓값
- xG Buildup :	 체인에서 슈팅과 키패스에 관여하지 않은 선수에게 주는 값
- xG 90 : 90분당 xG값
- NPxG 90 : 90분당 NPxG값
- xA 90 : 90분당 xA
- xG90 + xA90 : 90분당 공격포인트에 대한 기댓값
- NPxG90 + xA90 : 90분당 페널티킥 없는 공격포인트 기댓값(더 객관적 지표)
- xGChain90 :	 90분당 xG Chain값
- xGBuildup90 : 90분당 xG Buildup값
## Credit
- @LDHIUM