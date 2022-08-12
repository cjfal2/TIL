import sys
input = sys.stdin.readline

N = int(input())
L = []
for _ in range(N):
    Z = []
    x , y = map(int,input().split())
    Z.append(x)
    Z.append(y)
    L.append(Z)
L.sort(key=lambda x:x[0])
L.sort(key=lambda x:x[1])
for i in L :
    print(*i)