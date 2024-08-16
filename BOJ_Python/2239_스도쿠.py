import sys; input = sys.stdin.readline

def back_tracking(idx):
    global flag

    if flag:
        return

    if idx == 81:
        for row in arr:
            print(''.join(map(str, row)))
            flag = True
        return

    i, j = divmod(idx, 9)

    if arr[i][j] > 0:
        back_tracking(idx + 1)
    else:
        s = set(range(1, 10))

        for c in range(9):
            s.discard(arr[i][c])

        for r in range(9):
            s.discard(arr[r][j])

        sr = i // 3 * 3
        sc = j // 3 * 3
        for dr in range(3):
            for dc in range(3):
                s.discard(arr[sr + dr][sc + dc])

        for n in sorted(s):
            arr[i][j] = n
            back_tracking(idx + 1)
            arr[i][j] = 0


arr = [list(map(int, input().strip())) for _ in range(9)]

flag = False

back_tracking(0)