T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr_N = [] # 이중 배열
    arr_M = [] # 행 열을 뒤집은 배열

    for i in range(N):
        arr_N.append(list(input())) 

    # 뒤집기
    arr_M = list(map(list, zip(*arr_N)))
    
    for i in arr_N: 
        if i[::-1] == i: 
            print("".join(i))
    for i in arr_M:
        if  i[::-1] == i:
            print("".join(i))