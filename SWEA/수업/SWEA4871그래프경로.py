def DFS(graph, start, visited):
    visited[start] = 1  #현재 위치  (tc1 : 1)
    for i in graph[start]:  # 현재위치에서 갈 수 있는 노드 (tc1 : 1일때는 4와 3)
        if visited[i] == 0:  # 다음 위치에 안갔다면
            DFS(graph, i, visited) # 재귀 호출

for TC in range(1, int(input())+1):
    V, E = map(int, input().split()) # V노드의 개수, E간선의 개수
    G = [[] for _ in range(V+1)] # 노드의 개수 + 1 만큼 graph생성 (인덱스를 편하게 주기위해)
    visited = [0] * (V+1)  # 방문한 노드를 체크하기 위한 같은 길이의 vis리스트
    for _ in range(E): # 인풋 값으로 노드 정보 입력 : 그래프 생성
        node, daum = map(int, input().split()) #노드의 연결된 다음 노드를 받음
        G[node].append(daum) # G의 노드위치(인덱스)에 다음 노드를 추가
    
    start, end = map(int, input().split())  # 마지막 인풋

    DFS(G, start, visited) #재귀 호출
    # case1의 경우 체크된 visited : [0,1,0,1,1,0,1]

    result = 0
    if visited[end] == 1: #end를 지나갔는지 확인 지나갔으면 1 아니면 0
        result += 1
    print(f'#{TC} {result}')