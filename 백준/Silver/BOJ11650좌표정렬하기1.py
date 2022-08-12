import sys
input = sys.stdin.readline
N=int(input())
A = []
for _ in range(N):
    L = list(map(int,input().split()))
    A.append(L)
A.sort(key=lambda x:x[1]) #열 기준 정렬
A.sort(key=lambda x:x[0]) #행 기준 정렬
for i in A:
    print(*i)