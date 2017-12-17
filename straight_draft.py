# Run an analysis of a straight draft. Players select based on seed in each round

# TODO: make this all in numpy / pandas rather than this crap. Coding on a plane
#       without docs sucks.

import os
import itertools
import pandas as pd

import CONFIG

# load the data file
df = pd.read_csv('data/tables/all.csv', dtype = {'season': 'str'})

# create a list of the picks
data = {
    'position': list(range(1, CONFIG.PLAYERS*CONFIG.PICKS+1)),
    'player' : list(x % 6 + 1 for x in range(CONFIG.PLAYERS*CONFIG.PICKS))
}

picks_df = pd.DataFrame(data)
df = pd.merge(df, picks_df)


season_totals = df.groupby(['season', 'player'])['points'].sum()
strategy_mean = season_totals.groupby('season').std().mean()

print("The mean for the straight draft stragey is {0}".format(strategy_mean))
