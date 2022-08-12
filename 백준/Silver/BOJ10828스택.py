N = int(input())

L = []
for i in range(N):
    cmd = list(map(str,input().split()))
    if len(cmd) > 1 :
        L.insert(0,(int(cmd[1])))
    elif cmd[0] == 'pop' :
        if L == [] :
            print(-1)
        else:
            A = L.pop(0)
            print(A)
    elif cmd[0] == 'size':
        print(len(L))
    elif cmd[0] == 'empty':
        if L == [] :
            print(1)
        else :
            print(0)
    elif cmd[0] == 'top':
        if L == [] :
            print(-1)
        else :
            print(L[0])
