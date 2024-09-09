def back_tracking(team, opponent):
    global ans

    if ans == 1:
        return

    if team == 5:
        ans = 1
        return

    for wdl in range(3):    # win-draw_lose
        opponent_wdl = 2 - wdl

        tmp_result[team][wdl] += 1
        tmp_result[opponent][opponent_wdl] += 1

        if tmp_result[team][wdl] <= result[team][wdl] and tmp_result[opponent][opponent_wdl] <= result[opponent][opponent_wdl]:
            if opponent == 5:
                back_tracking(team + 1, team + 2)
            else:
                back_tracking(team, opponent + 1)

        tmp_result[team][wdl] -= 1
        tmp_result[opponent][opponent_wdl] -= 1


def check():
    for i in range(6):
        if sum(result[i]) != 5:
            return

    back_tracking(0, 1)


ans_lst = []

for _ in range(4):
    lst = list(map(int, input().split()))

    result = [lst[i:i + 3] for i in range(0, 18, 3)]
    tmp_result = [[0] * 3 for _ in range(6)]
    ans = 0

    check()

    ans_lst.append(ans)

print(*ans_lst)