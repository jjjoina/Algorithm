r = set()
for _ in range(10):
    n = int(input())
    r.add(n % 42)
print(len(r))