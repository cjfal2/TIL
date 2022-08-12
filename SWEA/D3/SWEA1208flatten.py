import sys
sys.stdin = open('flatten.txt','r')
#######################
def mymax(arr):   #max 구현하기
    mymax1 = arr[0]   #첫번째 원소를 일단 가장 큰 수로 등록
    for i in arr:
        if mymax1 < i :
            mymax1 = i
    return mymax1   # 비교하면서 가장 큰 수 반환

def mymin(arr):  #min 구현하기
    mymin1 = arr[0]  #첫번째 원소를 일단 가장 작은 수로 등록
    for i in arr:
        if mymin1 > i :
            mymin1 = i
    return mymin1  # 비교하면서 가장 작은 수 반환

def where_idx(arr,target):  # .index 구현하기
    counts = -1    # 인덱스를 찾아야하므로 -1부터 시작해서 바로 1씩 추가
    for i in arr :
        counts += 1
        if i == target : 
            return counts  # 타겟이라면 인덱스를 반환
            break   # 없으면 None

for tc in range(10):
    dump = int(input())
    box = list(map(int,input().split()))
    for _ in range(dump):  #덤프의 수만큼 반복
        box[where_idx(box,mymax(box))] = mymax(box)-1     #가장 많은 박스에서 하나 뺌
        box[where_idx(box,mymin(box))] = mymin(box)+1     #가장 적은 박스에서 하나 더함
    print(f'#{tc+1} {mymax(box)-mymin(box)}')   #가장큰거와 작은거의 차이를 출력
