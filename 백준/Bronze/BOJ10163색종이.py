import sys
input = sys.stdin.readline

N = int(input())

base = [[0]*1001 for _ in range(1001)]

for a in range(1,N+1) :
    x,y,w,h = map(int,input().split())
    print(type(x),type(y),type(w),type(h))
    for n in range(y,y+h):  
        
        base[n][x:x+w] = [a]*w

for i in range(1, N+1):
    co = 0
    for hang in base:
        co += hang.count(i)
    print(co)