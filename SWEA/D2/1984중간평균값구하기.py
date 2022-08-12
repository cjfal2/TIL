TC = int(input())

for tc in range(1,TC+1):
    nums = list(map(int,input().split()))
    nums.pop(nums.index(max(nums)))
    nums.pop(nums.index(min(nums)))
    print(f'#{tc} {sum(nums)/len(nums):.0f}')