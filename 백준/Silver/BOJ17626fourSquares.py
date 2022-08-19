N = int(input())
L = [0] * 50001
for i in range(1,N+1):
    Q = []
    k = 1
    while i >= k**2 :
        Q.append(L[i-k**2])
        k += 1
    L[i] = min(Q)+1
print(L[N])