import sys; input = sys.stdin.readline

w_lst = [int(input()) for _ in range(10)]
k_lst = [int(input()) for _ in range(10)]

w_lst.sort(reverse=True)
k_lst.sort(reverse=True)

print(sum(w_lst[:3]), sum(k_lst[:3]))