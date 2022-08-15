import sys
while True :
    N = input()
    if N == '0' :
        break
    elif N==N[::-1]:
        print('yes')
    else :
        print('no')