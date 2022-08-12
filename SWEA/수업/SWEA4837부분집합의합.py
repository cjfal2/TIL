TC = int(input())

for tc in range(1,TC+1):
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    N,K = map(int,input().split())

    counts = 0
    for i in range(1<<12):
        M = []
        for j in range(12):
            if i&(1<<j):
                M.append(A[j])
            
        if len(M) == N and sum(M) == K:
            counts += 1
        if len(M) > N :
            break

    if counts == 0 :
        print(f'#{tc} 0')
    else :
        print(f'#{tc} {counts}')