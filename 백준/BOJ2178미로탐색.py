N,M = map(int,input().split())
maze = [[0]*(M+2)]+[[0]+list(map(int,input()))+[0] for _ in range(N)]+[[0]*(M+2)]
for i in maze:
    print(*i)
news = [[-1,0],[1,0],[0,-1],[0,1]] # 상0하1좌2우3
x,y,d = 1,1,0
while x != N and y != M :
    
