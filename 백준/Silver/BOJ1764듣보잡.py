def binary(a,key):
    low_idx = 0
    high_idx = len(a)-1
    while low_idx <= high_idx:
        mid_idx = int((low_idx + high_idx)/2)
        if key == a[mid_idx]:
            return key
            break
        elif key < a[mid_idx] :
            high_idx = mid_idx - 1
        elif key > a[mid_idx]:
            low_idx = mid_idx + 1
    return 0

N , M = map(int,input().split())
n = [input() for _ in range(N)]
m = sorted([input() for _ in range(M)])

L = []
for name in n :
    G = binary(m,name)
    if G != 0 :
        L.append(G)
print(len(L))
L.sort()
for i in range(len(L)):
    print(L[i])