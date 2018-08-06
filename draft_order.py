# establish the player draft order using player names as the random seed

import random

players = ['Theaker', 'Dorian', 'Reddy', 'Walsh', 'Jones']
players.sort()

random.seed('ArsenalBournemouthBrightonBurnleyCardiff CityChelseaCrystal PalaceEvertonFulhamHuddersfieldLeicesterLiverpoolMan CityMan UnitedNewcastleSouthamptonTottenhamWatfordWest HamWolverhampton')
random.shuffle(players)

print("Pick Order:")
for x in players:
    print(x)
