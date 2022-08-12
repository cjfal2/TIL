import sys
# input = sys.stdin.readline
sys.stdin = open('sample.txt','r')
######
N , M = map(int,input().split())
L = {}
for z in range(1,N+1):
    K = input().rstrip()
    L[K] = str(z)
J = {v:k for k,v in L.items()}

i = 0
while i < M :
    Z = input().rstrip()
    if Z in L :
        print(L.get(Z))
    else :
        print(J.get(Z))
    i += 1