N, K = map(int,input().split())
L = []
for i in range(1,N+1):
    if not N%i:
        L.append(i)
        
if K > len(L):
    print(0)
else :
    print(L[K-1])