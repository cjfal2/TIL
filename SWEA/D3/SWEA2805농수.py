for tc in range(int(input())):
    N = int(input())
    F = [list(map(int,input())) for _ in range(N)]
    Q = []
    for x in range(N):
        if x <= N//2 :
            A = (2*x+1)//2
            Q.append(sum(F[x][N//2-A:N//2+A+1]))
        else:
            v = N-x-1
            A = (2*v+1)//2
            Q.append(sum(F[x][N//2-A:N//2+A+1]))
    print(f'#{tc+1} {sum(Q)}')
