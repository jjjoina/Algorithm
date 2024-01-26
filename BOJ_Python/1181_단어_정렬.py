N = int(input())
words = set()
for _ in range(N):
    words.add(input())
# list로 형변환
words = list(words)
words.sort(key=lambda x: (len(x), x))
for w in words:
    print(w)