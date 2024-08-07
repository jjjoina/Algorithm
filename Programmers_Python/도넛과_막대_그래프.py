'''
추가한 노드 : 진입 차수가 0 and 진출 차수가 2 이상
추가한 노드에서 다음 노드(w)로 탐색
w가 어떤 그래프에 속하느냐에 따라 answer 업데이트
    막대 모양 : 진출 차수가 0인 정점 존재
    8자 모양 : 진출 차수가 2인 정점 존재
    도넛 모양 : (else 혹은) 모든 정점의 진출 차수가 1
'''

from collections import deque

def get_graph_type(v, adj_d, in_out_degree):
    q = deque()
    visited = set()
    q.append(v)
    visited.add(v)

    while q:
        v = q.popleft()

        if in_out_degree[v][1] == 0:
            return 2

        if in_out_degree[v][1] == 2:
            return 3

        for w in adj_d[v]:
            if w not in visited:
                q.append(w)
                visited.add(w)

    return 1


def solution(edges):
    answer = [0, 0, 0, 0]

    adj_d = {}
    in_out_degree = {}

    for a, b in edges:
        if a not in adj_d:
            adj_d[a] = {b}
        else:
            adj_d[a].add(b)

        if a not in in_out_degree:
            in_out_degree[a] = [0, 1]
        else:
            in_out_degree[a][1] += 1

        if b not in in_out_degree:
            in_out_degree[b] = [1, 0]
        else:
            in_out_degree[b][0] += 1

    for v, degrees in in_out_degree.items():
        if degrees[0] == 0 and degrees[1] >= 2:
            answer[0] = v
            break

    for w in adj_d[answer[0]]:
        answer[get_graph_type(w, adj_d, in_out_degree)] += 1

    return answer