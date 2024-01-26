# 풀이 2.
# 0이 나오려면 2와 5가 합쳐져야 함
# 2는 뭐 차고 넘치므로 5의 개수를 세는 게 중요
N = int(input())
# 1~n까지 5가 몇 번 나왔나?
ans = 0
while N > 0:
    ans += N // 5
    N //= 5
print(ans)

# N = int(input())
# N_fac = 1
# for i in range(1, N+1):
#     N_fac *= i
    
# ans = 0
# while N_fac % 10 == 0:
#     N_fac //= 10
#     ans += 1
# print(ans)