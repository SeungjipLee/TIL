from collections import deque
import sys
sys.stdin = open('sample_input (1).txt')

def BFS(S, G, V):
    final = 0
    visited = [0]*(V+1)
    Que = deque()
    Que.append(S)
    visited[S] = 1
    while Que:
        now = Que.popleft()
        for next in range(V+1):
            if Board[now][next] == 1 and visited[next] == 0:
                Que.append(next)
                visited[next] = visited[now] + 1
                if next == G:
                    return visited[next] - 1

    return final

Testcase = int(input())
for test in range(Testcase):
    V, E = map(int, input().split())
    Board = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        Board[a][b] = 1
        Board[b][a] = 1
    S, G = map(int, input().split())
    print(f'#{test+1}', BFS(S, G, V))