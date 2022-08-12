TC = int(input())

for tc in range(TC) :
    N, M = map(int,input().split())
    L = []
    for n in range(N):
        L.append(input())
    #행 기준으로 M길이 순회
    for i in range(N): #행 을 순회

        for j in range(N-M+1): #행에서 문자열을 찾음
            G = L[i][j:j+M]
            if G == G[::-1]:
                print(f'#{tc+1} {G}')

    #열 기준으로 M길이를 순회
    for k in range(N):  #열 을 순회
        H = ''
        for d in range(N): #행 을 순회하면서 세로 문자열 H를 생성
            H += L[d][k]

        for j in range(N-M+1): #H에서 문자열을 찾음
            G = H[j:j+M]
            if G == G[::-1]:
                print(f'#{tc+1} {G}')