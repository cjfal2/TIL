t = int(input())

score_arr = []
total = [0 for i in range (t)]

for _ in range (t):
    score = int(input())
    score_arr.append(score)

if t ==1:
    print(score_arr[0])
    exit()
    
elif t==2:
    print(max(score_arr[1], score_arr[0]+score_arr[1]))
    exit()

total[0] = score_arr[0]
total[1] = max(score_arr[1], score_arr[0]+score_arr[1])
total[2] = max(score_arr[0]+score_arr[2], score_arr[1]+score_arr[2])

for i in range(3, t): # 3번째 부터 일정한 규칙
    total[i] = max(total[i-2]+score_arr[i], total[i-3]+score_arr[i-1]+score_arr[i])
print(total[-1])