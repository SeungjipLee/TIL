'''
1. 그래프에서 최소 비용문제
    : 모든 정점을 연결하는 가선들의 가중치의 합이 최소가 되는 트리
    : 두 정점 사이의 최소 비용의 경로 찾기
2. 신장 트리
    : n 개의 정점으로 이루어진 무방향 그래프에서 n개의
    정점과 n-1개의 간선으로 이루어진 트리
3. 최소 신장 트리
    : 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의
    가중치의 합이 최소인 신장트리

<최소 신장 트리를 어떻게 구할까?>
1. 완전탐색? -> 너무 많은 경우
2. 특정 정점에서 출발하여 내가 갈 수 있는 점들 중
제일 짧은 곳으로 가자.(그리디 + BFS? -> 우선순위 큐)
3. 전체 간선들 중에서 제일 가중치가 적은 곳부터 선택(그리디)

위의 2번 방법 -> prim 알고리즘
[Prim Algorithm]
 : 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서
 MST를 만들어 가는 방식
 : 서로소인 2개의 집합(2 disjoint-sets)정보를 유지
'''

'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''

import heapq

def prim(start):
    heap = []
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 1)
    heapq.heappush(heap, 2)

    print(heapq.heappop(heap))
    print(heapq.heappop(heap))
    print(heapq.heappop(heap))

V, E = map(int, input().split())
# 인접행렬
graph = [[0]*V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w
    graph[t][f] = w

prim(0)