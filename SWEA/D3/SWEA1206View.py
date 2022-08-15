import sys
sys.stdin = open('SWEA1206View.txt','r')
#############인풋#################
for tc in range(1,11):
    N = int(input())
    arr = list(map(int,input().split()))
###############################
    counts = 0   # 세대 수를 셀 변수 설정
    for i in range(2,N-2):   # 범위를 앞 뒤 두칸 씩 제외하고 설정
        my = 256   # 최소값을 저장해야 하므로 256으로 설정 (최대 255이기 때문)
        if (0 < arr[i] - arr[i-2]) and (0 < arr[i] - arr[i-1]) and (0 < arr[i] - arr[i+1]) and (0 < arr[i] - arr[i+2]):    #만약 나보다 큰 건물이 하나라도 있는지 검사
            my_list = [arr[i] - arr[i-2],arr[i] - arr[i-1], arr[i] - arr[i+1] , arr[i] - arr[i+2]]   #내 층수에서 양 옆 4건물의 층수를 뺀 것을 리스트로 저장
            for j in my_list: # 그 리스트의 최소가 되는 값이 필요하므로 if를 통해 최솟값을 찾아줌
                if my >= j :
                    my = j
        else :   # 큰건물이 하나라도 있으면 0을 저장
            my = 0
        
        counts += my  # 세대수에 반영
    print(f'#{tc} {counts}')