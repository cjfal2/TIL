import sys
input = sys.stdin.readline

N,M = map(int,input().strip().split())

idpw = {}
for _ in range(N):
    domain , pw = input().strip().split()
    idpw[domain] = pw


for _ in range(M):
    print(idpw.get(input().strip()))