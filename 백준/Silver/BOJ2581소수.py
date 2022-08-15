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

if sosu == [] :
    print(-1)
else :
    print(sum(sosu))
    print(min(sosu))