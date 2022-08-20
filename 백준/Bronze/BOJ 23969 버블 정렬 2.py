import sys
input = sys.stdin.readline

def LEN(arr):
    co = 0
    for _ in arr:
        co += 1
    return co

def bb(arr):
    N =LEN(arr)
    z = 0
    for i in range(N-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                z += 1
                arr[j],arr[j+1]=arr[j+1],arr[j]
                if z == K:
                    return arr
    return [-1]

M,K = map(int,input().strip().split())
L = list(map(int,input().strip().split()))

print(*bb(L))