def solve(B):
    # 거꾸로 B에서 A를 만드는 법을 생각해보자
    ans = 1
    while True:
        if B < A: return -1
        if B == A: return ans 

        # 두 가지 선택지 중 하나
        if B % 10 == 1:     # 끝자리 수가 1이면
            B //= 10        # 오른쪽에서 1을 지운다. (10의 몫을 취한다.)
            ans += 1
        elif B % 2 == 0:    # 짝수면
            B //= 2         # 2로 나눈다.
            ans += 1
        else:               # 다른 숫자면
            return -1       # -1을 반환한다.


A, B = map(int, input().split())
print(solve(B))