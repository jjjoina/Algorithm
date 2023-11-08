N = int(input())

dp = [[1, 1, 1]]

for _ in range(N-1):
    temp = [0, 0, 0]
    temp[0] = (dp[-1][0] + dp[-1][1] + dp[-1][2]) % 9901
    temp[1] = (dp[-1][0] + dp[-1][2]) % 9901
    temp[2] = (dp[-1][0] + dp[-1][1]) % 9901
    dp.append(temp)

print(sum(dp[-1]) % 9901)