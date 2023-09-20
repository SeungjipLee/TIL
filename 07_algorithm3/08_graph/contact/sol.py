from collections import deque
import sys
sys.stdin = open('a.txt')

def BFS(S):
    global final
    Q = deque([S])
    visited[S] = 1
    while Q:
        now = Q.popleft()
        for next in adj[now]:
            if visited[next]==0:
                Q.append(next)
                visited[next] = visited[now]+1
                if visited[next] >= final:
                    final = visited[next]


for tc in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    final = 0
    for i in range(0, N, 2):
        a, b = arr[i], arr[i+1]
        adj[a].append(b)
    visited = [0]*101
    BFS(S)
    ans = 0
    for j in range(101):
        if visited[j] == final:
            ans = j
    print(f'#{tc}', ans)