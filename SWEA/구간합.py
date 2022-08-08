T = int(input())
for i in range(1,T+1):
    N,M = map(int,input().split())
    nums = list(map(int,input().split()))
    countbig = 0
    countsmall = 0
    for idx in range(len(nums)-M):
        A = sum(nums[idx:idx+M])
        print(A)
        countbig = max(countbig,A)
        countsmall = min(countbig,A)

    print(f'#{i} {countbig-countsmall}')