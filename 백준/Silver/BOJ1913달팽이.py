# N = int(input())
N = 7
# K = int(input())
K = 35

nesw = [[1,0],[0,1],[-1,0],[0,-1]] # 상 우 하 좌

base = [[0 for _ in range(N)] for _ in range(N)]  # NxN의 베이스

num , i , j , direction = N**2+1,0,0,0

while num > 1:
    num -= 1
    base[i][j] = num
    
    if num == K :
        x,y = i+1,j+1
    
    i += nesw[direction][0]  #설정한 방향으로 전진 (direction: 상0 우1 하2 좌3)
    j += nesw[direction][1]
    if i < 0 or j < 0 or i >= N or j >= N or base[i][j] != 0: # 범위를 넘어갔거나, 0인 숫자가 아닌경우
        i -= nesw[direction][0]  #방향을 전환하기 위해서 다시 돌려놓음
        j -= nesw[direction][1]
        direction += 1     #방향전환
        if direction == 4 :
            direction = 0  #방향은 0~3 이므로 4를 다시 0으로 저장
        i += nesw[direction][0] #바꾼 방향으로 다시 전진
        j += nesw[direction][1]
    

for i in range(N):
    print(*base[i])
print(x,y)