import sys
sys.stdin = open('sample.txt','r')

TC = int(input())
for tc in range(TC):
    N = int(input())
    L = list(map(int,input().split()))

    for i in range(N-1):
        minidx = i # 구간의 맨 앞을 최소값으로 지정
        for j in range(i+1, N):  # 실제 최소값 인덱스 찾기
            if L[minidx] > L[j]:  # 리스트의 최소값으로 지정한것이 뒤(i+1 자리)에 다른 요소보다 크면
                minidx = j    # 그 작은 요소의 인덱스를 저장
        L[i],L[minidx] = L[minidx],L[i] # 최소값을 구간 맨 앞으로

    print(f'#{tc+1}',*L)