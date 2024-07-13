import sys; input = sys.stdin.readline
import heapq

problems_hard = []
problems_easy = []
# solved = set()
levels = [0] * 100001

N = int(input())
for _ in range(N):
    P, L = map(int, input().split())
    heapq.heappush(problems_hard, [-L, -P])
    heapq.heappush(problems_easy, [L, P])
    levels[P] = L

M = int(input())
for _ in range(M):
    command = input().split()

    if command[0] == 'recommend':
        problems = problems_hard if command[1] == '1' else problems_easy
        # while (abs(problems[0][1]), abs(problems[0][0])) in solved:
        while levels[abs(problems[0][1])] != abs(problems[0][0]):   # 이미 푼 문제인 경우
            heapq.heappop(problems)
        print(abs(problems[0][1]))

    elif command[0] == 'add':
        P = int(command[1])
        L = int(command[2])
        heapq.heappush(problems_hard, [-L, -P])
        heapq.heappush(problems_easy, [L, P])
        levels[P] = L

    else:
        P = int(command[1])
        # solved.add((P, levels[P]))
        levels[P] = 0