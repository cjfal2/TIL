import sys
sys.stdin = open('0808prac1.txt','r')

di = [0,1,0,-1]
dj = [1,0,-1,0]

TC = int(input())
for tc in range(TC):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]
    L = []
    
    for i in range(N):
        for j in range(N):
            hap = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N :
                    hap += abs(arr[ni][nj] - arr[i][j])
            L.append(hap)
    print(f'#{tc+1} {sum(L)}')