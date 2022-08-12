while True: 
    A , B = map(int,input().split())
    if (A or B) == 0:
        break
    elif A > B :
        print("Yes")
    elif A <= B :
        print("No")