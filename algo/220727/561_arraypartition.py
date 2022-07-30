#n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라
nums = [1,4,3,2]  #4
nums.sort()
print(sum(nums[::2]))
