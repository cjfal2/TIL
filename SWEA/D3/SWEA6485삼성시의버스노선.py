import sys
sys.stdin = open('SWEA6485삼성시의버스노선.txt','r')
############
TC = int(input())

for tc in range(TC):
    N = int(input())
    nosun = [0]*N   # 노선의 범위를 저장할 변수
    
    for i in range(N):
        A = list(map(int,input().split()))
        nosun[i] = A   #이중리스트 생성
    
    P = int(input())
    stop = [0] * P
    for i in range(P):     # 인풋 P를 받고 정류장 번호를 받는 리스트를 만들어줌
        stop[i] = int(input())
    nosun_num = [0] * P
    for ns in nosun :
        for k in range(ns[0],ns[1]+1):
            for m in range(P):
                if stop[m] == k:
                    nosun_num[m] += 1
    print(f'#{tc+1}',end=' ')
    print(*nosun_num)
