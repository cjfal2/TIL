hr , minute = map(int,input().split())
need_hr , need_min = divmod(int(input()),60)
after_hr = hr + need_hr
after_min = minute + need_min

if after_min > 59 :
    after_hr += 1
    after_min -= 60   

if after_hr > 23 :
    after_hr = after_hr % 24

print(after_hr , after_min)