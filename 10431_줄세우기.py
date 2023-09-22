P = int(input())
for _ in range(P):
    T, *heights = map(int, input().split())
    
    stack1 = []
    stack2 = []
    ans = 0
    for i in range(20):
        while stack1 and stack1[-1] > heights[i]:
            stack2.append(stack1.pop())
            ans += 1
        stack1.append(heights[i])
        while stack2:
            stack1.append(stack2.pop())
    print(T, ans)