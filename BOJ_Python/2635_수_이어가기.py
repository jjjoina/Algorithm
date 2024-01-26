import sys; input = sys.stdin.readline

N = int(input())

ans_num = 0
ans_lst= []
for i in range(N//2+1, N+1):
    lst = [N, i]
    while True:
        new = lst[-2] - lst[-1]
        if new < 0: break
        lst.append(new)
    if ans_num < len(lst):
        ans_num = len(lst)
        ans_lst = lst
    
print(ans_num)
print(*ans_lst)