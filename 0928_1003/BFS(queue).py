'''
BFS란?
'너비 우선 탐색'으로
Graph Traversal 과정에서 갈림길을 만났을 때,
모든 갈림길로 한 발자국씩 간 다음 위치를 저장하며,
같은 level 에 있는 것들을 차례대로 방문하여 탐색하는 것

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

from collections import deque

# N : 노드의 개수 / M : 간선의 개수 / V : 출발점
N, M, V = map(int, input().split())
# 연결 정보를 담을 이중 리스트
Adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    Adj[a].append(b)
    Adj[b].append(a)


def BFS(V):
    Q = deque([V])
    visited = [0]*(N+1)
    while Q:
        now = Q.popleft()
