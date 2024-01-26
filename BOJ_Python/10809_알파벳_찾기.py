# index 쓰지 말고 풀어보자
S = input()
ans = [-1] * 26
for i in range(len(S)):
    # j : c는 j번째 알파벳
    j = ord(S[i]) - ord('a')
    # 아직 바뀌지 않은 경우만 변경 (처음 등장하는 위치만 기록)
    if ans[j] == -1:
        ans[j] = i
print(*ans)