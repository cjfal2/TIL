for i in range(1,int(input())+1):
    a , b = map(int,input().split())
    c = a + b
    if c > 23:
        c = c%24
    
    print(f'#{i} {c}')