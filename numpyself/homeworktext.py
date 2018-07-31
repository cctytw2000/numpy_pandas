import numpy as np
players = [56, 8, 19, 14, 6, 71]
teams = ["apple", "organse", "pineapple", "big apple", "bananna", "cherry"]
players_arr = np.array(players)
teams_arr = np.array(teams)
#answer
playersmax = np.argmax(players_arr)
print(teams_arr[[playersmax]])
print(players_arr[[playersmax]])
