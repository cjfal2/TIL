for tc in range(int(input())):
    N,K = map(int,input().split())
    scores = list(map(int,input().split()))
    scores.sort(reverse=True)
    print(f'#{tc+1} {sum(scores[:K])}')