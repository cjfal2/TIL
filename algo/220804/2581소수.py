N = int(input())
M = int(input())


sosu = []
for i in range(N,M+1) :
    L = []
    for j in range(1,i+1):
        if i%j == 0 :
            L.append(j)
    if len(L) == 2 :
        sosu.append(L[-1])
print(sosu)
print(sum(sosu),min(sosu))