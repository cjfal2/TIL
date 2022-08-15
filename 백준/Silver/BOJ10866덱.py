# import sys
# input=sys.stdin.readline 

import sys
sys.stdin = open('sample.txt','r')

L = []
for i in range(int(input())):
    A = list(input().split())
    if A[0] == 'push_front':
        L.insert(0,int(A[1]))
        print(A[1])
    elif A[0] == 'push_back':
        L.append(int(A[1]))
        print(A[1])
    elif A[0] == 'pop_front':
        if len(L) == 0 :
            print(-1)
        else :
            L.pop(0)
    elif A[0] == 'pop_back':
        if len(L) == 0 :
            print(-1)
        else :
            L.pop(-1)
    elif A[0] == 'size':
        print(len(L))
    elif A[0] == 'empty':
        if len(L) == 0:
            print(1)
        else :
            print(0)
    elif A[0] == 'front':
        if len(L) == 0 :
            print(-1) 
        else:
            print(L[0])
    elif A[0] == 'back':
        if len(L) == 0 :
            print(-1) 
        else:
            print(L[-1])