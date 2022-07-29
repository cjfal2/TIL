T = int(input())

for i in range(1,T+1):
    N , M = map(int,input().split())
    A = list(map(int,input().split()))

    L = []
    for k in range(len(A)-M+1) :
        MM = 0
        for m in range(M):
            MM += A[k+m] 
        L.append(MM)

    big = max(L)
    small = min(L)
    print(f'#{i} {big-small}')