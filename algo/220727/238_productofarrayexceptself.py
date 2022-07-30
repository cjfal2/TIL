# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라
nums = [1,2,3,4]  # [24,12,8,6]
#  나눗셈 금지
newnums = nums[:]
L = [0]*len(nums)
for i in range(len(nums)):
    gop = 1
    newnums.pop(i)    
    for k in newnums:
        L[i] = gop = gop * k
    newnums = nums[:]
print(L)
