import sys
input = sys.stdin.readline

for _ in range(int(input())):
    H , W , N = map(int,input().split())
    if N%H == 0 :
        if N//H < 10 :
            print(str(H)+'0'+str(N//H))
        else :
            print(str(H)+str(N//H))
    else : 
        if N//H < 9 :
            print(str(N%H)+'0'+str((N//H)+1))
        else :
            print(str(N%H)+str((N//H)+1))