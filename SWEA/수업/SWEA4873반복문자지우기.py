for tc in range(int(input())):
    text = list(input())
    L = []
    while True :
        if len(text) > 0:
            L.append(text[0])
            text.pop(0)

        if len(L) > 1 :
            if L[-2] == L[-1]:
                L.pop()
                L.pop()
        if len(text) == 0:
            break
    print(f'#{tc+1} {len(L)}')