import sys
sys.stdin = open('sample.txt','r')

for tc in range(int(input())):
    sudoku = [list(map(int,input().split())) for _ in range(9)]
    
    fail = 0
    for n in range(9):
        # 행탐색  n : 행
        if sum(sudoku[n]) != 45 :
            print(f'#{tc+1} 0')
            fail += 1
            break
        
        # 열탐색
        yeal = []
        for m in range(9): # n : 열, m : 행
            yeal.append(sudoku[m][n])
        if sum(yeal) != 45 :
            print(f'#{tc+1} 0')
            fail += 1
            break
    N,M = 9,3
    # 3x3 네모 탐색
    if fail != 1 :
        cube = []
        for x1 in range(0,N-M+1,3):
            for y1 in range(0,N-M+1,3):
                su = 0
                for x2 in range(M):
                    for y2 in range(M):
                        su += sudoku[x1+x2][y1+y2]
                cube.append(su)
        for i in cube:
            if i != 45 :
                print(f'#{tc+1} 0')
                fail += 1
                break
            
    if fail == 0:
        print(f'#{tc+1} 1')