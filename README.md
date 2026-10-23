Football League Simulator based on user chosen teams and attributes:
(different outcome every time!)

Attributes determining team strength: 
- team level between 1 & 10 (10 highest)
- team injury status between 1 & 10 (10 highest)
- team luck - RNG for added random component

Determination of individual match scores
- goals scored by each team simulated from a normal distribution with means linked to their relative strength and variance 1
- goals scored based on a maximum of the normal result and zero to avoid negative scores

Class libraries used:
- numpy - for random luck generation and normal distribution simulation
- itertools - to identify all match permutations in the league (home & away)
- pandas - for a sorted DataFrame of the final league standings
- tabulate - for presentation purposes

Possible enhancements:
- using a discrete probability distribution such as Poisson to simulate goals scored
- creating an easier user setup for teams
- displaying individual match results in the output

Example output:
```
⚽ Welcome to the Football Simulator! ⚽

╒════╤═══════════╤══════════╤═════╤═════╤═════╤══════╤══════╤══════╤═══════╕
│    │ Team      │   PLAYED │   W │   D │   L │   GF │   GA │   GD │   PTS │
╞════╪═══════════╪══════════╪═════╪═════╪═════╪══════╪══════╪══════╪═══════╡
│  1 │ Liverpool │        6 │   3 │   2 │   1 │   19 │   10 │    9 │    11 │
├────┼───────────┼──────────┼─────┼─────┼─────┼──────┼──────┼──────┼───────┤
│  2 │ Man City  │        6 │   3 │   2 │   1 │   14 │   11 │    3 │    11 │
├────┼───────────┼──────────┼─────┼─────┼─────┼──────┼──────┼──────┼───────┤
│  3 │ Arsenal   │        6 │   1 │   3 │   2 │   13 │   17 │   -4 │     6 │
├────┼───────────┼──────────┼─────┼─────┼─────┼──────┼──────┼──────┼───────┤
│  4 │ Man Utd   │        6 │   1 │   1 │   4 │   10 │   18 │   -8 │     4 │
╘════╧═══════════╧══════════╧═════╧═════╧═════╧══════╧══════╧══════╧═══════╛
```

