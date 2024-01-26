# 내장 함수 사용
# pypy로 제출해야 시간 초과 안 뜬다.
# N = int(input())
# arr = [int(input()) for _ in range(N)]
# arr.sort()
# for n in arr:
#     print(n)

# 풀이 2. input() 대신에 sys.stdin.readline() 사용
import sys
N = int(input())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()
for n in arr:
    print(n)