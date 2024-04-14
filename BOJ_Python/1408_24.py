start_hour, start_min, start_sec = map(int, input().split(':'))
end_hour, end_min, end_sec = map(int, input().split(':'))

start = start_hour * 3600 + start_min * 60 + start_sec
end = end_hour * 3600 + end_min * 60 + end_sec

ans = end - start
if ans < 0 :
    ans += 24 * 3600
    
print(f'{ans // 3600:02}:{ans % 3600 // 60:02}:{ans % 60:02}')