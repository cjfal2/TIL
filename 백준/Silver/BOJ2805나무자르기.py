def cut(mid):
    co = 0
    for i in trees:
        if i >= mid:
            co += i - mid
    return co >= want

N, want = map(int, input().split())
trees = sorted(list(map(int, input().split())))

start = 0
end = max(trees)

while start <= end:
    mid = (start+end)//2
    if cut(mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)