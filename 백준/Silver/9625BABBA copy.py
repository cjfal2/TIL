# import sys
# input = sys.stdin.readline
# N = int(input())

# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# if N == 1 :
#     print(0,1)
# else :
#     print(fib(N-1),fib(N))



import sys
input = sys.stdin.readline
N = int(input())

def fib(n):
    a,b = 1,1
    if n==1 or n==2:
        return 1
        
    for i in range(1,n):
        a,b = b, a+b

    return a

if N == 1 :
    print(0,1)
else :
    print(fib(N-1),fib(N))