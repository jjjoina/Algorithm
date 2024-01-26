import sys; input = sys.stdin.readline

for _ in range(int(input())):
    lst = list(map(int, input().split()))
    even_lst = [n for n in lst if n % 2 == 0]
    print(sum(even_lst), min(even_lst))