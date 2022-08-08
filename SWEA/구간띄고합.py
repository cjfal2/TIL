for i in range(1,int(input())+1):
    A,B = map(int,input().split())

    L = 0
    for j in range(A,B+1):
        L += sum(list(map(int,str(j))))

    print(f'#{i} {L}')