import sys
input = sys.stdin.readline
N = int(input())

L = [1]
M = []
for i in range(2,N+1):
    M.append(i)
    if len(M) == 6*len(L):
        L.append(i)
        M = []
        
if N == 1 :
    print(1)
elif M != [] :
    print(len(L)+1)
else:
    print(len(L))
#################시간초과
N=int(input())
counts=0
six=1
while True:
    six+=6*counts
    counts+=1
    if six>=N: break
print(counts)
