def start(arr):
    '''
    x : 행 좌표
    y : 열 좌표
    return : x,y
    '''
    for x in range(N+2):
        for y in range(N+2):
            if arr[x][y] == 2:
                return x,y

news = [[-1,0],[0,1],[1,0],[0,-1]] # 상0 우1 하2 좌3

for _ in range(10):
    N = 100
    tc = int(input())-1
    maze = [[1 for _ in range(N+2)]] + [[1] + list(map(int,input())) +[1] for _ in range(N)] + [[1 for _ in range(N+2)]] # 상하좌우에 벽을 세움
    
    visit = [[] for _ in range(N+2)]  # 같은 배열의 visit을 만드는데 이미 1이면 True 아니면 False
    for x in range(N+2):
        for y in range(N+2):
            if maze[x][y] == 1:
                visit[x].append(True)
            else:
                visit[x].append(False)

    dix = 0 # 방향
    x,y = start(maze)
    sx,sy = x,y
    # print(x,y) -> tc1 : 5,4
    res = 0
    galim = [] #갈림길 좌표를 넣어줄 스택
    
    while 1:
        visit[x][y] = True # 지나간 곳은 visit에서 True로

        if visit[x+1][y] and visit[x-1][y] and visit[x][y-1] and visit[x][y+1] and x==sx and y==sy: #사방이 다 True 인데 시작점이면 종료
            break
        
        if visit[x+1][y] and visit[x-1][y] and visit[x][y-1] and visit[x][y+1]: # 사방이 다 True인데 시작점이 아니면 갈림길 스택을 확인
            if galim: # 갈림길스택에 뭔가 있으면
                x,y = galim[-1] # 갈림길스택의 맨 마지막으로 이동하고
                galim.pop() # 그 좌표는 팝
            else:
                x,y = sx,sy # 갈림길스택에 뭔가 없으면, 시작점으로

        if (visit[x+1][y] + visit[x-1][y] + visit[x][y-1] + visit[x][y+1]) < 3: # 사방을 둘러보았을 때 갈 수 있는 길(False)이 2개이상이면 갈림길이므로 스택에 푸시 (True가 3개,4개면 길이 1개거나 막다른길) 
            galim.append([x,y])

        #-------이동------#
        x += news[dix][0]  
        y += news[dix][1]
        if maze[x][y] == 3: # 이동했는데 도착점이면 끝내기
            res = 1 
            break
        if maze[x][y] == 1 or visit[x][y]: # 방문했던 지점이거나 1이라는 벽이면 빠꾸
            x -= news[dix][0]
            y -= news[dix][1]
            dix += 1
            if dix == 4:
                dix = 0
            
    print(f'#{tc+1} {res}')