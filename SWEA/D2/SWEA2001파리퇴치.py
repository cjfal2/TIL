import sys
sys.stdin = open('sample.txt','r')

for tc in range(int(input())):
    N ,M = map(int, input().split())
    wall = [list(map(int,input().split())) for _ in range(N)]
  
    flykill = []
    for x1 in range(N-M+1):
      for y1 in range(N-M+1):
        fly = 0
        for x2 in range(M):
          for y2 in range(M):
            fly += wall[x1+x2][y1+y2]
        flykill.append(fly)

    print(f'#{tc+1} {max(flykill)}')