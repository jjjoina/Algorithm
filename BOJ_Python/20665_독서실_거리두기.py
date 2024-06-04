import sys; input = sys.stdin.readline

OUT = 0
IN = 1

def get_best_seat():
    # 독서실을 이용하는 사람이 없으면 1번 좌석을 선호
    if not using_seats:
        return 1
    
    max_dist = 0
    seat = None
    
    for s in range(1, N+1):
        if s in using_seats:
            continue
        
        min_dist = 987654321
        for us in using_seats:
            dist = abs(s - us)
            if min_dist > dist:
                min_dist = dist
        
        if max_dist < min_dist:
            max_dist = min_dist
            seat = s
            
    return seat


N, T, P = map(int, input().split())
reservations = []
for i in range(1, T+1):
    in_t, out_t = input().split()
    
    if in_t == out_t:
        continue
    
    in_t = int(in_t[:2]) * 60 + int(in_t[2:])
    out_t = int(out_t[:2]) * 60 + int(out_t[2:])
    
    reservations.append([in_t, IN, out_t, i])
    reservations.append([out_t, OUT, i])
    
reservations.sort()

using_seats = set()
person_seat = [0] * (T+1)
prev_t = 9 * 60
ans = 0

for r in reservations:
    if r[1] == IN:
        bs = get_best_seat()
        using_seats.add(bs)
        person_seat[r[3]] = bs

        if bs == P:
            ans += r[0] - prev_t
    
    else:
        s = person_seat[r[2]]
        using_seats.remove(s)
        person_seat[r[2]] = 0
        
        if s == P:
            prev_t = r[0]

ans += 21 * 60 - prev_t
        
print(ans)