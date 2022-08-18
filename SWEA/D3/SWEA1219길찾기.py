def DFS(graph, start, visited):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            DFS(graph, i, visited)
        
for tc in range(1, 11):
    TC, N = map(int, input().split())
    G = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visited = [0] * 100

    # 그래프 생성
    for i in range(N):
        graph[G[2*i]].append(G[2*i+1])

    DFS(graph, 0, visited)

    result = 0
    if visited[99] == 1:
        result = 1
    print(f'#{TC} {result}')