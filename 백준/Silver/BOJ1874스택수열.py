import sys
input = sys.stdin.readline

from collections import deque

mystack = deque()
want = deque()
PM = deque()

N = int(input())

A = [int(input()) for _ in range(N)]
for a in A:
    want.append(a)

nums = [i for i in range(1,N+1)]

i = 0
while True :
    i += 1
    if len(mystack) > 0 and want[0] == mystack[-1]:
        want.popleft()
        mystack.pop()
        PM.append('-')
    
    else :
        if len(nums) > 0 :
            mystack.append(nums[0])
            nums.pop(0)
            PM.append('+')
    
    if len(want) == 0:
        break
    if i > N*3 :
        print('NO')
        break
if i <= N*3 :
    print(*PM,sep='\n')