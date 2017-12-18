# establish the player draft order using player names as the random seed

import random

players = ['Theaker', 'Dorian', 'Reddy', 'Walsh', 'Geary', 'Jones']
players.sort()

random.seed(''.join(players))
random.shuffle(players)

print("Pick Order:")
for x in players:
    print(x)
