numbers = set(range(1, 31))
for _ in range(28):
    numbers.remove(int(input()))
print(min(numbers))
print(max(numbers))