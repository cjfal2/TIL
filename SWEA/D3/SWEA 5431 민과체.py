for tc in range(int(input())):
    N,K=map(int,input().split())
    L = list(map(int,input().split()))
    stu = [i for i in range(1,N+1)]
    F = []
    for i in stu:
        if i not in L:
            F.append(i)
    print(f'#{tc+1}',*F)