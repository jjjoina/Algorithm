import sys; input = sys.stdin.readline

def get_mind_dist(mbti1, mbti2):
    mind_dist = 0
    for i in range(4):
        if mbti1[i] != mbti2[i]:
            mind_dist += 1
    return mind_dist


def solve():
    N = int(input())
    lst = input().split()
    
    cnt_dict = {}
    max_3_lst = []
    ans = 987654321
    
    for mbti in lst:
        if cnt_dict.get(mbti, 0) >= 3:
            return 0
        cnt_dict[mbti] = cnt_dict.get(mbti, 0) + 1
        max_3_lst.append(mbti)

    l = len(max_3_lst)
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                mind_dist = get_mind_dist(max_3_lst[i], max_3_lst[j]) + get_mind_dist(max_3_lst[j], max_3_lst[k]) + get_mind_dist(max_3_lst[i], max_3_lst[k])
                if ans > mind_dist:
                    ans = mind_dist

    return ans


T = int(input())
for _ in range(T):
    print(solve())