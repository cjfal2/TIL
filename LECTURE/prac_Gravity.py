import sys
sys.stdin = open('prac_Gravity.txt','r')
###########

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    boxes = list(map(int, input().split()))
    
    maxnum = 0 # 최대 낙차값 넣을 변수
    counts = 0 # 현재 위치의 박스보다 높이가 같거나 큰 박스 개수
    for i in range(n):
        for j in range(n): # 현재 위치의 박스부터
            if boxes[j] >= boxes[i]: # 높이가 같거나 더 큰 박스가 있다면 (본인부터 세는구나)
                counts += 1          # counts가 바닥? 의 높이를 높여주는구나
        if n-i-counts > maxnum:   # n-i-counts : 9-0-1 = ?? 
            maxnum = n-i-counts
        counts = 0

    print(f'#{tc} {maxnum}')

# 어차피 빈칸만큼 떨어지니까 그 범위를 구함
# 자신이랑 작거나 큰 박스를 카운트에 더해서