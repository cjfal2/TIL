import sys
input = sys.stdin.readline

def dfs(G,s,vis):
    vis[s] = 1
    for i in G[s]:
        if vis[i] == 0 :
            dfs(G,i,vis)

V , E = map(int,input().rstrip().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    nod , daum = map(int,input().rstrip().split())
    G[nod].append(daum)
    G[daum].append(nod)

vis_list = []
for z in range(1,V+1):
    vis_test = [0] * (V+1)
    dfs(G,z,vis_test)
    vis_list.append(vis_test)
    vis_test = [0] * (V+1)

a = []
for g in vis_list:
    if g not in a :
        a.append(g)

print(len(a))