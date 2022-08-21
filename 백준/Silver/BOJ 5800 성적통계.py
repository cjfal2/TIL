def bb(arr):
    MAX = 0
    for i in range(N-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    for i in range(N-1):
        if MAX < arr[i+1]-arr[i]:
            MAX = arr[i+1]-arr[i]
    return arr[0],arr[-1],MAX

K = int(input())
for cls in range(K):
    L = list(map(int,input().split()))
    N = L[0]
    L = L[1:]
    a,b,c = bb(L)
    print(f'Class {cls+1}')
    print(f'Max {b}, Min {a}, Largest gap {c}')