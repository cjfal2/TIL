N = int(input())
FIND = input()
maze = [['#' for _ in range(102)] for _ in range(102)] #최대 49까지 이므로 넉넉하게 생성

news = [[1,0],[0,1],[-1,0],[0,-1]] # 하 우 상 좌
# 우 좌 : y 이동  , 상 하 x 이동

face = 0  # 0하 1우 2상 3좌
x,y = 51 , 51
maze[x][y] = '.' #일단 시작점

whereIcanGo = []
whereIcanGo.append([x, y])

for move in FIND:
    if move == 'R':
        face -= 1
        if face == -1 :
            face = 3

    elif move == 'L':
        face += 1
        if face == 4 :
            face = 0

    elif move == 'F':
        x += news[face][0]
        y += news[face][1]

    maze[x][y] = '.'
    whereIcanGo.append([x, y])

min_deca_n = 103
min_deca_m = 103
for n,m in whereIcanGo:
    if n < min_deca_n:
        min_deca_n = n
    if m < min_deca_m:
        min_deca_m = m

max_deca_n = -1
max_deca_m = -1

for n,m in whereIcanGo:
    if n > max_deca_n:
        max_deca_n = n
    if m > max_deca_m:
        max_deca_m = m

re_maze = maze[min_deca_n:max_deca_n+1]
for idx,k in enumerate(re_maze):
    re_maze[idx] = k[min_deca_m:max_deca_m+1]
for i in re_maze:
    print(*i,sep='')