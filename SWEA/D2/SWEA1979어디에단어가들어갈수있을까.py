import sys
sys.stdin = open('sample.txt','r')

for tc in range(int(input())):
    N,K = map(int,input().split())
    words = [list(map(int,input().split()))+[0] for _ in range(N)]+[[0]*(N+1)]
    
    counts = 0  #들어갈 수 있는 칸
    # 우측 검색
    for n in range(N) : #같은 행에 대하여
        kan = 0 #칸수
        for m in range(N): #열을 순회 
            if words[n][m] == 1:  #1이면 1을 더하고
                kan += 1
                if kan == K and words[n][m+1] == 0:  #칸수가 원하는 칸인데 다음이 0이면
                    counts += 1  #들어갈 수 있는 칸에 1을 더하고
                    kan = 0  #칸수를 초기화
            else :
                kan = 0
    # 하측 검색
    for m in range(N) : #같은 열 에 대하여
        kan = 0
        for n in range(N) : #행을 순회
            if words[n][m] == 1:
                kan += 1
                if kan == K and words[n+1][m] == 0:  #칸수가 원하는 칸인데 다음이 0이면
                    counts += 1  #들어갈 수 있는 칸에 1을 더하고
                    kan = 0  #칸수를 초기화
            else :
                kan = 0
    print(f'#{tc+1} {counts}')