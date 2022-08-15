T = int(input())

def binary(a,key):
    start = 1
    end = len(a)
    counts = 0
    while start <= end:
        counts += 1
        middle = start + (end - start)//2
        if key == middle:  #검색 성공
            return counts
            
        elif key < middle:
            end = middle
        else:
            start = middle
    return counts # 검색 실패

for i in range(T):
    P, key_a , key_b = map(int,input().split())
    P = [j for j in range(1,P+1)]
    A = binary(P,key_a)
    B = binary(P,key_b)
    
    if A < B :
        print(f'#{i+1} A')
    elif A > B :
        print(f'#{i+1} B')
    else :
        print(f'#{i+1} 0')