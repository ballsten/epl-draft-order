import os
import pandas
from collections import defaultdict

COLS = ["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR"]

seasons = []

def create_table(file):
    season_date = file.split("/")[-1].split(".")[0]
    print("processing season", season_date)
    season = pandas.read_csv(file, sep=",", usecols=COLS)
    table = defaultdict(lambda: { 'points':0, 'goaldiff': 0})
    for index, row in season.iterrows():
        table[row.HomeTeam]['points'] += 3 if row.FTR == "H" else 1 if row.FTR == "D" else 0
        table[row.AwayTeam]['points'] += 3 if row.FTR == "A" else 1 if row.FTR == "D" else 0
        table[row.HomeTeam]['goaldiff'] += row.FTHG - row.FTAG
        table[row.AwayTeam]['goaldiff'] += row.FTAG - row.FTHG

    output = list()
    for k, v in table.items():
        v['team'] = k
        output.append(v)

    df = pandas.DataFrame(sorted(output, key=lambda x: x['points']+(200+x['goaldiff'])/100, reverse=True))
    df['season'] = season_date
    df = df[['season', 'team', 'points', 'goaldiff']]
    seasons.append(df)

for root, dirs, files in os.walk("data/matches"):
    for file in files:
        create_table(os.path.join(root, file))

pandas.concat(seasons).to_csv('data/tables/all.csv', quoting=2, index=False)
