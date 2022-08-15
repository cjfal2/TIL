for tc in range(int(input())):
    N = int(input())
    A = N//10
    if A%2 : # 홀수
        tape = 0
        for i in range(0,A,2):
            tape += 2**i
    else : # 짝수
        tape = 1
        for i in range(1,A,2):
            tape += 2**i
    print(f'#{tc+1} {tape}')