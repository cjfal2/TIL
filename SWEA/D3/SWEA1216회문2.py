import sys
sys.stdin = open('sample.txt','r')

for tc1 in range(10):
    tc = int(input())
    A = [input() for _ in range(100)]
    
    M = 0  #문자의 길이
    long_M = 0
    while M < 100:
        M += 1
        ### 행 기준으로 M길이 순회
        for i in range(100): #행 을 순회

            for j in range(100-M+1): #행에서 문자열을 찾음
                G = A[i][j:j+M]
                if G == G[::-1]:
                    long_M = M
                    break
        ### 열 기준으로 M길이를 순회
        for k in range(100):  #열 을 순회
            H = ''
            for h in range(100): #행 을 순회하면서 해당 열의 세로 문자열 H를 생성
                H += A[h][k]

            for j in range(100-M+1): #H에서 문자열을 찾음
                G = H[j:j+M]
                if G == G[::-1]:
                    long_M = M
                    break
    print(f'#{tc} {long_M}')