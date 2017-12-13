# Run an analysis of a straight draft. Players select based on seed in each round

# TODO: make this all in numpy / pandas rather than this crap. Coding on a plane
#       without docs sucks.

import os
import itertools
import pandas as pd

import CONFIG

# create the pick array, index is the player number (0..x-1)
picks = ((x+y*CONFIG.PLAYERS for y in range(CONFIG.PICKS)) for x in range(CONFIG.PLAYERS))

# load the data file
df = pd.read_csv('data/tables/all.csv', dtype = {'season': 'str'})

# is just testing on one season for now
SEASON = '0001'
df = df.query('season == "{0}"'.format(SEASON))

result = []
for x in picks:
    total = 0
    for y in x:
        total += int(df.query('position == {0}'.format(y+1))['points'])

    result.append(total)

print(result)
