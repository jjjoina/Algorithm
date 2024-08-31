import sys; input = sys.stdin.readline

num_of_weights = int(input())
weights = list(map(int, input().split()))
num_of_beads = int(input())
beads = list(map(int, input().split()))

sum_weights = sum(weights)
is_possible = [False] * (sum_weights + 1)
is_possible[0] = True

for weight in weights:
    tmp = []

    for i in range(sum_weights + 1):
        if is_possible[i]:
            tmp.append(i + weight)
            tmp.append(abs(i - weight))

    for w in tmp:
        is_possible[w] = True

for bead in beads:
    if bead <= sum_weights and is_possible[bead]:
        print('Y', end=' ')
    else:
        print('N', end=' ')