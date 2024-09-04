from collections import deque

def bfs():
    q = deque()
    visited = [[-1, 0] for _ in range(200000)]  # visited[i] = [최단 시간, 방법의 수]
    q.append(N)
    visited[N] = [0, 1]

    while q:
        v = q.popleft()

        if visited[K][0] != -1 and visited[v][0] > visited[K][0]:
            break

        for nv in [v + 1, v - 1, 2 * v]:
            if 0 <= nv < 200000:
                if visited[nv][0] == -1:    # 처음 방문하는 경우
                    visited[nv][0] = visited[v][0] + 1
                    visited[nv][1] += visited[v][1]
                    q.append(nv)
                elif visited[nv][0] == visited[v][0] + 1:   # 다른 방식의 최단 시간으로 방문하는 경우
                    visited[nv][1] += visited[v][1]

    return visited[K]


N, K = map(int, input().split())

ans_time, ans_cnt = bfs()

print(ans_time)
print(ans_cnt)