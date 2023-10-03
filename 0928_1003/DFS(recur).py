'''
DFS를 재귀로 구현하려면 어떻게 해야할까?

재귀 코드를 작성하는 세가지 순서
1. 종료 조건
2. 재귀 작성
3. 얻고 싶은 데이터 작성

[input 값]
4 5 1
1 2
1 3
1 4
2 4
3 4
[output 값]
1 2 4 3
'''

# N : 노드의 개수 / M : 간선의 개수 / V : 출발점
N, M, V = map(int, input().split())
# 연결 정보를 담을 이중 리스트
Adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    Adj[a].append(b)
    Adj[b].append(a)

# visited 가 바깥에 있어야 재귀를 돌며 초기화 안됨
visited = [0]*(N+1)
# 언제 종료할 것인가? -> 그래프를 갈 수 있는만큼 다 가면
def DFS(V):
    visited[V] = 1
    print(V, end=' ')
    for next in Adj[V]:
        if visited[next] == 0:
            DFS(next)
    return

DFS(V)