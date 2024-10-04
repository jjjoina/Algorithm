import sys
sys.setrecursionlimit(3000)

dir_to_char = ["d", "l", "r", "u"]
di = [1, 0, 0, -1]
dj = [0, -1, 1, 0]
answer = "impossible"
stack = []

def solution(n, m, x, y, r, c, k):
    def dfs(i, j, depth):
        global answer

        if answer != "impossible":
            return

        if depth == k:
            if i == r and j == c:
                answer = ''.join(stack)
            return

        if depth + abs(r - i) + abs(c - j) > k:
            return

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if (0 <= ni < n and 0 <= nj < m):
                stack.append(dir_to_char[d])
                dfs(ni, nj, depth + 1)
                stack.pop()

    x -= 1
    y -= 1
    r -= 1
    c -= 1

    if (k - (abs(r - x) + abs(c - y))) % 2 == 1:
        return answer

    for d in range(4):
        ni = x + di[d]
        nj = y + dj[d]

        if (0 <= ni < n and 0 <= nj < m):
            stack.append(dir_to_char[d])
            dfs(ni, nj, 1)
            stack.pop()

    return answer