'''
DFS란?
'깊이 우선 탐색'으로
Graph Traversal 과정에서 갈림길을 만났을 때,
그 위치를 저장해나가다가 막히는 지점이 오면,
가장 최근에 저장해둔 위치로 돌아가 다른 방향으로 탐색


[input 값]
4 5 1
1 2
1 3
1 4
2 4
3 4
[output 값]
1 4 3 2
'''


# N : 노드의 개수 / M : 간선의 개수 / V : 출발점
N, M, V = map(int, input().split())
# 연결 정보를 담을 이중 리스트
Adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    Adj[a].append(b)
    Adj[b].append(a)

# DFS 정의
def DFS(V):
    stack = [V]
    visited = [0]*(N+1)
    while stack:
        now = stack.pop()
        if visited[now] == 0:
            print(now, end=' ')
            visited[now] = 1
        for next in Adj[now]:
            if visited[next] == 0:
                stack.append(next)

DFS(V)