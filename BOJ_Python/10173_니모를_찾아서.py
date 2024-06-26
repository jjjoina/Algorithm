import sys; input = sys.stdin.readline

while True:
    s = input().strip()
    if s == 'EOI':
        break
    print('Found' if 'nemo' in s.lower() else 'Missing')