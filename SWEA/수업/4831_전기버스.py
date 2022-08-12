T = int(input())

for t in range(1,T+1):
    battery_full , N , M = map(int,input().split())
    charger = list(map(int,input().split()))                    #정류장의 인덱스를 리스트로 받음
    bus_line = [0]*(N+1)                                        #버스라인의 뼈대 구성 (시작점 포함하여 N+1)
    for i in charger:                                           #뼈대에 충전기설치구역 표시(1)
        bus_line[i] = 1        

    charge_count = 0                                            #충전한 횟수를 셀 카운트 변수
    battery_now = battery_full                                  #현재 배터리의 양을 저장할 변수
    
    for idx, bst  in enumerate(bus_line) :                      #현재 버스의 위치(idx)와 충전기 설치 여부(0 or 1)를 불러옴
                                                                #bst(설치여부)가 0일때와 1일때를 따로 체크
        if bst == 0 :                                           #충전기가 없을 경우
            if idx == N :                                     
                print(f'#{t} {charge_count}')                   #도착점일 경우 마무리
                break
            else :                                              #도착점이 아닐 경우
                if battery_now == 0 :                           #현재 배터리가 0일 경우 0을 출력하라
                    print(f'#{t} 0')
                    break
                else :                                          #현재 배터리가 0보다 클 경우
                    battery_now -= 1                            #한 칸 전진하라

        if bst == 1 :                                           #충전기가 있을 경우
            if idx == N :                                       #도착점일 경우
                print(f'#{t} {charge_count}')                   #마무리
                break
            else :                                              #도착점이 아닐 경우
                if (1 in bus_line[idx+1:]) :                    #이번충전소 다음에 충전소가 있으면
                    next_charger = bus_line[idx+1:].index(1)+1  #다음 충전소까지의 거리를계산
                else :                                          #다음 충전소가 없다면
                    if N-idx > battery_now :                    #남은거리보다 남은 배터리가 작으면
                        charge_count +=1                        #충전을 한 번 하고
                        print(f'#{t} {charge_count}')           # 마무리
                        break
                    else :
                        print(f'#{t} {charge_count}')           # 남은거리보다 남은 배터리가 많거나 같으면 그냥 마무리
                        break
                if battery_now < next_charger :                 #현재 남은 배터리양이 다음 있을 충전소까지의 거리보다 작을 경우
                    battery_now = battery_full                  #배터리를 충전하고
                    charge_count += 1                           #충전 횟수 증가
                    battery_now -= 1                            #한칸 전진
                else :                                          #현재 남은 배터리양이 다음 있을 충전소까지의 거리보다 크거나 같을 경우
                    battery_now -= 1                            #한칸 전진