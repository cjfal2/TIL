TC = int(input())

moum = 'aeiou'

for tc in range(TC):
    A = input()
    for i in moum :
        A = A.replace(i,'')
    print(f'#{tc+1} {A}')
    