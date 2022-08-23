N= int(input())
if N == 1:
    print('*')
else:
    for x in range(1,N+1):
        print(' '*(N-x),'*',' '*((x-1)*2-1),sep='',end='')
        if x == 1:
            print()
        else:
            print('*')