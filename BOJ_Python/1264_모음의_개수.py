import sys; input = sys.stdin.readline

vowels = {'a', 'e', 'i', 'o', 'u',
          'A', 'E', 'I', 'O', 'U',}

while True:
    s = input().strip()
    if s == '#': break
    
    ans = 0
    for c in s:
        if c in vowels:
            ans += 1
    
    print(ans)