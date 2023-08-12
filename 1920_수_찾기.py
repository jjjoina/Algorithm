# 풀이 3. 이분탐색
import sys; input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()
for b in B:
    # 이분탐색
    s = 0
    e = N-1
    flag = 0
    while s <= e:
        m = (s+e) // 2
        if A[m] == b:
            flag = 1
            break
        elif A[m] > b:
            e = m - 1
        else:
            s = m + 1
    print(flag)



# # 풀이 2. 딕셔너리 활용
# import sys; input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# B = list(map(int, input().split()))

# dic = {} 
# for a in A:
#     dic[a] = 1
# for b in B:
#     print(dic.get(b, 0))


# # 풀이 1. 예상대로 시간 초과
# import sys; input = sys.stdin.readline

# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# B = list(map(int, input().split()))

# for b in B:
#     if n in A: print(1)
#     else: print(0)