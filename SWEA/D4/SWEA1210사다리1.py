import sys
sys.stdin = open('sample.txt','r')

def whereis2(arr):
    counts = -1
    for i in arr:
        counts += 1
        if i == 2 :
            return counts

news = [[0,-1],[1,0],[0,1]] # 좌0 하1 우2  (위로는 안감)

for _ in range(10):
    tc = int(input())
    ladder = [[0]+list(map(int,input().split()))+[0] for _ in range(100)][::-1] + [0 for _ in range(102)]
    # 시작점 설정
    m = whereis2(ladder[0])
    n = 0
    
    # 방향 설정 (일단 아래방향 부터)
    direction = 1
    # 사다리 타기 시작
    while n != 99 :
        # 한칸 전진
        n += news[direction][0]
        m += news[direction][1]
        
        # 진행 방향이 아래일 경우
        if direction == 1 :
            # 우측 확인 해서 1이면
            if ladder[n][m+1] == 1 :
                direction = 2
            # 좌측 확인 해서 1이면
            elif ladder[n][m-1] == 1 :
                direction = 0
        # 진행 방향이 우/좌측일 경우
        elif direction == 2 or direction == 0:
            # 아래측을 확인해서 1이면
            if ladder[n+1][m] == 1 :
                direction = 1

    print(f'#{tc} {m-1}')