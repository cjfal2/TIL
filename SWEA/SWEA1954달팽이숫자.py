import sys
sys.stdin = open('달팽이숫자.txt','r')

from pprint import pprint
########################################################
eswn = [[0,1],[1,0],[0,-1],[-1,0]] # 우 하 좌 상

TC = int(input())

for tc in range(TC):
    N = int(input())
    base = [[0 for _ in range(N)] for _ in range(N)]  # NxN의 베이스
    num , i , j , direction = 0,0,0,0   #저장할 숫자, 행 , 열 , 방향
    
    while num < N**2:
        num += 1
        base[i][j] = num
        i += eswn[direction][0]  #설정한 방향으로 전진 (direction: 우0 하1 좌2 상3)
        j += eswn[direction][1]
        if i < 0 or j < 0 or i >= N or j >= N or base[i][j] != 0: # 범위를 넘어갔거나, 0이아닌 숫자가 있는경우
            i -= eswn[direction][0]  #방향을 전환하기 위해서 다시 돌려놓음
            j -= eswn[direction][1]
            direction += 1     #방향전환
            if direction == 4 :
                direction = 0  #방향은 0~3 이므로 4를 다시 0으로 저장
            i += eswn[direction][0] #바꾼 방향으로 다시 전진
            j += eswn[direction][1]
        # 반복

    print(f'#{tc+1}')
    for i in range(N):
        print(*base[i])