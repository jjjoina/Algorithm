import sys; input = sys.stdin.readline

scores = [0] * 3
winning_times = [0] * 3
prev_time = 0
winning_team = 0

N = int(input())
for _ in range(N):
    team, time = input().split()
    team = int(team)
    time = list(map(int, time.split(':')))
    time = time[0] * 60 + time[1]
    
    winning_times[winning_team] += time - prev_time
    
    prev_time = time
    scores[team] += 1
        
    if scores[1] > scores[2]:
        winning_team = 1
    elif scores[2] > scores[1]:
        winning_team = 2
    else:
        winning_team = 0

winning_times[winning_team] += 48 * 60 - prev_time

for i in range(1, 3):
    print(f'{winning_times[i]//60:02}:{winning_times[i]%60:02}')