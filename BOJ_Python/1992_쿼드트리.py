import sys; input = sys.stdin.readline

def get_status(si, ei, sj, ej):
    all_zero = all_one = True
    
    for i in range(si, ei+1):
        for j in range(sj, ej+1):
            if arr[i][j] == 1:
                all_zero = False
            else:
                all_one = False

            if not all_zero and not all_one:
                return all_zero, all_one
    
    return all_zero, all_one


def dc(si, ei, sj, ej):
    all_zero, all_one = get_status(si, ei, sj, ej)

    if all_zero:    # allzero인 경우
        ans.append('0')

    elif all_one:   # allone인 경우
        ans.append('1')
    
    else:
        mi, mj = (si+ei)//2, (sj+ej)//2
        div_idx = [[si, mi, sj, mj], 
                   [si, mi, mj+1, ej], 
                   [mi+1, ei, sj, mj], 
                   [mi+1, ei, mj+1, ej]]
        
        ans.append('(')
        for nsi, nei, nsj, nej in div_idx:
            dc(nsi, nei, nsj, nej)  # 각 구역마다 재귀 함수 호출
        ans.append(')')


N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]

ans = []
dc(0, N-1, 0, N-1)

print(''.join(ans))