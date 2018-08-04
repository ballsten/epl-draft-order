# Iterates through all combinations to determine the first. This is another
# bruteforce approach to the problem that determines the best combo for each
# round and then carries that result through.
# The limiting factor is that the first round will always run 1 through x

import itertools
import math
import pandas as pd
from progress_bar import printProgressBar

import CONFIG

# load the data file
df = pd.read_csv('data/tables/all.csv', dtype = {'season': 'str'})


def calculate_std(pick_order):
    # create a list of the picks
    data = {
        'position': list(range(1, len(pick_order)+1)),
        'player' : pick_order
    }

    picks_df = pd.DataFrame(data)
    all_df = pd.merge(df, picks_df)

    season_totals = all_df.groupby(['season', 'player'])['points'].sum()
    return season_totals.groupby('season').std().mean()

start = list(range(1, CONFIG.PLAYERS+1)) # first round goes in order

total_runs = math.factorial(CONFIG.PLAYERS) * (CONFIG.PICKS-1)
run_count = 1

print("There will be {0} total runs".format(total_runs))

for round in range(CONFIG.PICKS-1):
    rest = (x+1 for x in range(CONFIG.PLAYERS))
    perms = itertools.permutations(rest)

    best_combo = None
    best_result = 10000

    for rest in perms:
        picks = start + list(rest)
        result = calculate_std(picks)
        #printProgressBar(run_count, total_runs)
        run_count += 1
        if result < best_result:
            best_combo = picks
            best_result = result

    start = best_combo

print("Best result was: {0}".format(best_result))
print("Best combo was: {0}".format(best_combo))
