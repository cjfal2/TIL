def LEN(arr):
    co = 0
    for _ in arr:
        co+=1
    return co

def bb(arr):
    N = LEN(arr)
    z = 0
    for i in range(N-1,0,-1):
        for j in range(i):
            if arr[j+1] < arr[j]:
                z += 1
                arr[j],arr[j+1]=arr[j+1],arr[j]
                if z == K:
                    return arr[j],arr[j+1]
    return -1,-1


M,K = map(int,input().split())
L = list(map(int,input().split()))
A,B = bb(L)

if A == -1 :
    print(-1)
else :
    print(A,B)