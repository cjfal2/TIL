import sys
sys.stdin = open('sample.txt','r')

A,B = map(int,input().split())

if A == 1 :
    A = 2
for i in range(A,B+1):
    if i < 4 :
        print(i)
        continue
    else :
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사 -> 에라토스테네스의 체
        x = False
        for m in range(2, int(i ** 0.5) + 1):
            if i%m == 0:     
                x = True
                break
    if x :
        continue
    print(i)