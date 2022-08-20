def SUM(arr):
    co = 0
    for i in arr:
        co += i
    return co

def LEN(arr):
    co = 0
    for _ in arr:
        co += 1
    return co

def SC(arr):
    N = LEN(arr)
    z = 0
    for i in range(N-1,0,-1):
        MAX = i
        for j in range(i-1,-1,-1):
            if arr[j] > arr[MAX]:  
                MAX = j
        arr[i],arr[MAX]=arr[MAX],arr[i]
        if MAX != i :
            z += 1
            if z == K:
                return arr[MAX],arr[i]
    return -1,-1

N,K = map(int,input().split())

L = list(map(int,input().split()))

A,B = SC(L)
if A == -1 :
    print(-1)
else :
    print(A,B)