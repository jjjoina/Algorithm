N = int(input())
scores = list(map(int, input().split()))

# 최대값 구하기
max_score = scores[0]
for score in scores:
    if score > max_score:
        max_score = score

ans = 0
# 새로운 점수 구하기
for score in scores:
    ans += score / max_score * 100

# 평균 구하기
ans /= N
print(ans)