import sys
sys.stdin = open('koreauni.txt','r')
############
TC = int(input())
for tc in range(TC):
    #인풋
    N,M = map(int,input().split())  #N 행 , M 열 
    matrix = [list(map(int,input().split())) for _ in range(N)]
    
    real_max = 0
    #행 돌면서 긴거 찾기
    for n in range(N):
        x_max = 0
        for m in range(M):
            if matrix[n][m] == 1:
                x_max += 1
                if real_max <= x_max:
                    real_max = x_max
            else:
                x_max = 0
    #열 돌면서 긴거 찾기
    for m in range(M):
        y_max = 0
        for n in range(N):
            if matrix[n][m] == 1:
                y_max += 1
                if real_max <= y_max:
                    real_max = y_max
            else:
                y_max = 0
    print(f'#{tc+1} {real_max}')