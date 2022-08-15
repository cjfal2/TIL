for tc in range(int(input())):
    A = [list(input()) for _ in range(5)]
    # 가장 긴 길이를 찾음
    whatmax = 0
    for a in A :
        if whatmax < len(a) :
            whatmax = len(a)
    # 가장 긴 길이보다 짧으면 뒤에 모자란 만큼 * 추가
    for b in range(5) :
        if len(A[b]) < whatmax :
            A[b] = A[b] + ['*']*(whatmax-len(A[b]))
    
    sero = []
        
    for n in range(whatmax):
        for m in range(5):
            sero.append(A[m][n])
    
    serostr = ''.join(sero).replace('*','')

    print(f'#{tc+1} {serostr}')