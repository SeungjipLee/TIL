import sys
from pprint import pprint
sys.stdin = open('1967.txt')

def BFS(a):
    visited = [0]*(N+1)
    Queue = [a]
    mid = 0
    while Queue:
        now = Queue.pop(0)
        print(now)
        if visited[now] == 0:
            visited[now] = 1
        for next in range(N+1):
            if Adj[now][next] != 0 and visited[next] == 0:
                Queue.append(next)



N = int(input())
Adj = [[0]*(N+1) for _ in range(N+1)]
parent = [0]*(N+1)
for _ in range(N-2):
    a, b, c = map(int, input().split())
    Adj[a][b] = c
    Adj[b][a] = c
    parent[b] = a

a, b, c = map(int, input().split())
Adj[a][b] = c
Adj[b][a] = c
parent[b] = a
leaf = list(range(a+1, N+1))
pprint(Adj)
print(leaf)
for i in leaf:
    BFS(i)