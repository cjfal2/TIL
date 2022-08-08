N , K = map(int,input().split())

nums = []
for i in range(1,N+1):
    nums.append(i)

yose = []
nums_copy = nums[:]
for m in range(1,N+1):
    A = nums.pop(K-1)
    yose.append(A)
    nums=nums[K-1:]
