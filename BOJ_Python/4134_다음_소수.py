import sys; input = sys.stdin.readline

for _ in range(int(input())):
    ans = int(input())

    if ans < 2:
        print(2)
        
    else:
        while True:
            flag = True
            for i in range(2, int(ans**0.5)+1):
                if ans % i == 0:
                    flag = False
                    break
            if flag:
                print(ans)
                break
            ans += 1