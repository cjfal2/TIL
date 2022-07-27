nums = [2,7,11,15]
target = 26

hap_list = []
idx_list = []
for idx , num in enumerate(nums):
    for i in range(idx+1, len(nums)):
        hap_list.append(num + nums[i])
        idx_list.append([idx,i])
A = hap_list.index(target)
print(idx_list[A])