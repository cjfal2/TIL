import sys
sys.stdin = open('sample.txt','r')

from pprint import pprint
####################인풋#####################
TC = int(input())

for tc in range(TC):
    N = int(input())
    L = []
    for n in range(N):
        L.append(list(map(int,input().split())))
############################################
##################재밌는 0 만들기###########
    base = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
    
    for l in L :
        x1,y1,x2,y2,z = l[0],l[1],l[2],l[3],l[4]   #x좌표와 y좌표와 빨강여부를 추출
        for x in range(x1,x2+1):    #행 순회
            for y in range(y1,y2+1):    #열 순회
                base[x][y] = base[x][y]+1 #1을 쁠러스
                pprint(base)
    c2 = 0
    for i in base :
        c2 += i.count(2)
    print(f'#{tc+1} {c2}')