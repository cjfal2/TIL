import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

D = {}
for a in A :
    if a not in D :
        D[a] = 1
    else :
        D[a] = D[a] + 1

for b in B :
    if D.get(b) == None :
        print(0, end=' ')
    else :
        print(D.get(b), end=' ')
