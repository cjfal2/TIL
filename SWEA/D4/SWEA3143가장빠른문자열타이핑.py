for tc in range(int(input())):
    A, B = input().split()
    # A = A.replace(B,'@')
    print(f'#{tc+1} {len(A.replace(B,"@"))}')