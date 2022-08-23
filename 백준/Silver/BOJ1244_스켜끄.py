N = int(input())
switch = list(map(int,input().split()))
stu = int(input())
for _ in range(stu):
    S , num = map(int,input().split())

    if S == 1: # 남자
        for i in range(num-1,N,num): # num의 인덱스를 시작으로 num만큼 뛰면서 N까지
            switch[i]=(switch[i]+1)%2 # 변경
    
    else: # 여자
        switch[num-1]=(switch[num-1]+1)%2 # num자리는 무조건 바뀌니 바꿔줌
        k = 0
        while True: # 양쪽을 확인하는 while문 양쪽이 다르거나 범위를 넘어가면 중지
            k+=1
            if num-1-k==-1 or num-1+k==N:
                break
            if switch[num-1-k] == switch[num-1+k]: # 양쪽이 같으면 그 양쪽을 바꿔줌
                switch[num-1-k]=(switch[num-1-k]+1)%2
                switch[num-1+k]=(switch[num-1+k]+1)%2
            else:
                break
for a in range(0,N,20): # 20개씩 건너뛰면서 출력
    print(*switch[a:a+20]) 