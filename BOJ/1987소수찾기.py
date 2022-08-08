N = int(input())
A = list(map(int,input().split()))

counts = 0
for i in A :
    L = []
    for j in range(1,i+1):
        if i%j == 0 :
            L.append(j)
    if len(L) == 2 :
        counts += 1
print(counts)