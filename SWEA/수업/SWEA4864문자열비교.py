TC = int(input())

for tc in range(TC) :
    A = input()
    B = input()
    for i in range(len(B)-len(A)+1):
        if A == B[i:i+len(A)]:
            print(f'#{tc+1} 1')
            break
        if i == len(B)-len(A):
            if A != B[i:i+len(A)]:
                print(f'#{tc+1} 0')
