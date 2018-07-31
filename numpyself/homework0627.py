import numpy as np
import time
start = time.time()
players = [56, 8, 19, 14, 6, 71]
teams = ["apple", "organse", "pineapple", "big apple", "bananna", "cherry"]
players_arr = np.array([players])
teams_arr = np.array([teams])
print('Players總共有', players_arr.sum(), '人')
print('共有', teams_arr.size, '隊')
maxteam = players_arr == players_arr.max()
print('最多人的TEAM是', players_arr[maxteam], '人')
print('人數最多的隊伍是', teams_arr[[maxteam]])
max10team = players_arr > 10
print('人數大於10的隊伍是', teams_arr[[max10team]])
nocherryteam = teams_arr != 'cherry'
nocherrysum = players_arr[[nocherryteam]].sum()
print('除了CHERRY組別的加總人數', nocherrysum)
end = time.time()
print(end-start)
