# Run an analysis of a snake draft. Players select based on seed in each odd
# round and the reverse for even rounds

import pandas as pd

import CONFIG

# load the data file
df = pd.read_csv('data/tables/all.csv', dtype = {'season': 'str'})

# create a list of the picks
data = {
    'position': list(range(1, CONFIG.PLAYERS*CONFIG.PICKS+1)),
    'player' : list(x % 6 + 1 if (int(x / CONFIG.PLAYERS) + 1) % 2 > 0 else CONFIG.PLAYERS - x % CONFIG.PLAYERS for x in range(CONFIG.PLAYERS*CONFIG.PICKS))
}

print(int(7/2)%2)
print(data)

picks_df = pd.DataFrame(data)
df = pd.merge(df, picks_df)


season_totals = df.groupby(['season', 'player'])['points'].sum()
strategy_mean = season_totals.groupby('season').std().mean()

print("The mean for the straight draft stragey is {0}".format(strategy_mean))
