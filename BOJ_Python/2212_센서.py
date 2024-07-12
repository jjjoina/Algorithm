import sys; input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = sorted(map(int, input().split()))

intervals = sorted(sensors[i+1] - sensors[i] for i in range(N-1))

print(sum(intervals[:N-K]))