# EPL Draft order

The purpose of this project is to establish a fair draft order for an EPL wins
pool league. Such a league has a number of players (x), who select a number of
teams (y) in a predetermined order. At the end of the season, the total number
of points accumulated by each players teams is added together, the player with
the highest total is the winner. Goal difference is used to resolve any ties.

The product of x and y can not be greater than the number of teams in the league
to select from.

## Problem
Determine a fair drafting order. For the purpose of this analysis, it is assumed
that each player when choosing is making the optimal choice. Historical data
will be used back to the start of the EPL in 93/94.

A "fair order" is defined as one which the standard deviation is the lowest.
When comparing against historical data the average standard deviation is
considered.

### Straight draft
This draft is a seeded order 1 to x for each round.

### Snake draft
A snake draft runs through the seed order 1 to x and then reverses x to 1 for
the even rounds.

### Brute forced determined order
This approach starts with a seeded order 1 to x for the first round. It then
searches by brute force all possible combinations to determine which is the
fairest order.
