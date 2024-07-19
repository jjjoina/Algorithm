import sys; input = sys.stdin.readline

def simulation():
    for c, v in commands:
        if c == 1:
            if indegrees[v] > 0:
                return 'Lier!'
            cnt[v] += 1
            if cnt[v] == 1:
                for w in nexts[v]:
                    indegrees[w] -= 1
        else:
            if cnt[v] == 0:
                return 'Lier!'
            cnt[v] -= 1
            if cnt[v] == 0:
                for w in nexts[v]:
                    indegrees[w] += 1
    
    return 'King-God-Emperor'


N, M, K = map(int, input().split())
nexts = [[] for _ in range(N+1)]
indegrees = [0] * (N+1)
for _ in range(M):
    X, Y = map(int, input().split())
    nexts[X].append(Y)
    indegrees[Y] += 1
commands = [list(map(int, input().split())) for _ in range(K)]
cnt = [0] * (N+1)

print(simulation())