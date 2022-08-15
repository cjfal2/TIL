C,R = map(int,input().split())
where_mysit = int(input())
sit = [['*']*(R+2)] + [['*']+[0]*R+['*'] for _ in range(C)] + [['*']*(R+2)]
news = [[0,1],[1,0],[0,-1],[-1,0]] # 우 하 좌 상


x,y,direction = 1,1,0

z = 0 # 자리가 없을 경우를 판단할 변수
for num in range(1,C*R+1):
    # 자리 저장
    sit[x][y] = num
    if num == where_mysit :
        print(x,y)
        z += 1
        break
    # 전진
    x += news[direction][0]
    y += news[direction][1]
    # 벽이거나 이미 숫자가 있으면
    if sit[x][y] != 0 :
        # 빠꾸
        x -= news[direction][0]
        y -= news[direction][1]
        # 방향전환
        direction = direction+1
        if direction == 4:
            direction = 0
        # 바꾼 방향으로 전진
        x += news[direction][0]
        y += news[direction][1]

if z == 0 :
    print(0)