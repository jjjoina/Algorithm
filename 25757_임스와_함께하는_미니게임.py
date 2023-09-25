import sys; input = sys.stdin.readline

# 해당 게임을 하기 위해 필요한 사람의 수 (임스 제외)
dic = {'Y': 1, 'F': 2, 'O': 3}

N, game = input().split()
s = set()
for _ in range(int(N)):
    s.add(input().strip())

print(len(s) // dic[game])