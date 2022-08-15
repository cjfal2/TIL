N = int(input())

L = [0]*N

for i in range(N):
    A = input()
    L[i] = A
L = list(set(L))
L.sort()
L.sort(key=len)
print(*L,sep="\n")
    
