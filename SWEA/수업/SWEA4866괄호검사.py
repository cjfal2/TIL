for tc in range(int(input())):

    A = input()
    L = []
    for i in A:
        if i == '{' or i == '}' or i == '(' or i == ')':
            L.append(i)

        if len(L) > 1 :
            if L[-1] == ')' and L[-2] == '(' :
                L.pop()
                L.pop()
            elif L[-1] == '}' and L[-2] == '{' :
                L.pop()
                L.pop()

    if L == []:
        print(f'#{tc+1} 1')
    else :
        print(f'#{tc+1} 0')