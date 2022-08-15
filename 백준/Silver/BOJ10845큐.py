# import sys
# input=sys.stdin.readline 
L = []
for _ in range(int(input().strip())):
    A = list(input().strip().split())
    if A[0] == 'push' :
        L.append(A[1])
    elif A[0] == 'pop' :
        if len(L) == 0 :
            print(-1)
        else :
            print(L.pop(0))
    elif A[0] == 'empty' :
        if len(L) == 0 :
            print(1)
        else :
            print(0)
    elif A[0] == 'front' :
        if len(L) == 0 :
            print(-1)
        else :
            print(L[0])
    elif A[0] == 'back' :
        if len(L) == 0 :
            print(-1)
        else :
            print(L[-1])
    else :
        print(len(L))
        