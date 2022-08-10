import sys
sys.stdin = open('SUM.txt','r')

from pprint import pprint
#########
for _ in range(10):
    tc = int(input())
    
    matrix = [list(map(int,input().split())) for _ in range(100)]
    
    what_is_max = []
    # 행의 합을 모두 저장
    for i in range(100):
        what_is_max.append(sum(matrix[i]))

    # 열의 합
    
    for j in range(100):
        yeal = []
        for q in range(100):
            yeal.append(matrix[q][j])
        what_is_max.append(sum(yeal))
        

    # 대각 좌상우하
    for k in range(100):
        jsuh = []
        jsuh.append(matrix[k][k])
    what_is_max.append(sum(jsuh))
        
    # 대각 우상좌하
    z = 99
    for x in range(100):
        usjh = []
        usjh.append(matrix[x][z])
        z -= 1
    what_is_max.append(sum(usjh))

    print(f'#{tc}',end=' ')
    print(max(what_is_max))