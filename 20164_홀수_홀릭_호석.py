def solve(num, final_value):
    for d in num:
        if int(d) % 2: final_value += 1

    N = len(num)

    if N == 1:
        rst.append(final_value)

    elif N == 2:
        n_str = str(int(num[0]) + int(num[1]))
        solve(n_str, final_value)

    else:
        # 분할된 3개의 수들의 시작 인덱스 구하기
        # 0, i, j
        for i in range(1, N-1):
            for j in range(i+1, N):
                n_str = str(int(num[:i]) + int(num[i:j]) + int(num[j:]))
                solve(n_str, final_value)
        

lst = input()
rst = []
solve(lst, 0)
print(min(rst), max(rst))