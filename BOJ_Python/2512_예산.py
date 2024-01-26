import sys; input = sys.stdin.readline

def bs():
    s, e = 1, max(lst)
    while s <= e:
        m = (s+e) // 2  # m : 정답(상한액) 후보

        sum_v = 0       # 상한액을 m으로 잡았을 때의 예산 합
        for r in lst:
            sum_v += min(r, m)
        
        if sum_v < M:       # 1. 예산이 남는 경우
            s = m + 1       # 더 높은 범위 try
        
        elif sum_v == M:    # 2. 예산이 딱 맞는 경우
            return m

        else:               # 3. 예산이 부족한 경우
            e = m - 1       # 더 낮은 범위 try

    return e


N = int(input())
lst = list(map(int, input().split()))
M = int(input())    # 주어지는 총 예산
print(bs())