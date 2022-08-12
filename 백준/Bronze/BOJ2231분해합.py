N = int(input())

L = []
for i in range(1,N):
    if sum(list(map(int,str(i))))+i == N :
        L.append(i)
if L == [] :
    print(0)
else :
    print(min(L))