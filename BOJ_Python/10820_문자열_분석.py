while True:
    try:
        s = input()
    except:
        break
    
    rst = [0, 0, 0, 0]
    for c in s:
        if 'a' <= c <= 'z':
            rst[0] += 1
        elif 'A' <= c <= 'Z':
            rst[1] += 1
        elif '0' <= c <= '9':
            rst[2] += 1
        elif c == ' ':
            rst[3] += 1
    
    print(*rst)