s = list(input())

for i in range(len(s)):
    if 'a' <= s[i] <= 'z':
        s[i] = chr(ord(s[i]) + 13)
        if s[i] > 'z':
            s[i] = chr(ord(s[i]) - 26)
            
    elif 'A' <= s[i] <= 'Z':
        s[i] = chr(ord(s[i]) + 13)
        if s[i] > 'Z':
            s[i] = chr(ord(s[i]) - 26)

print(''.join(s))