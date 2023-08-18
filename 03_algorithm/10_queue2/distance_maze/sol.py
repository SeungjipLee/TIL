import sys
from collections import deque

sys.stdin = open('sample_input.txt')

# 델타 탐색(우 하 좌 상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]



def BFS(s, g, N):   # s : 출발점의 좌표, g : 도착점의 좌표, N : 보드 크기
    visited = [[0] * N for _ in range(N)]       # 방문체크판도 이중리스트로 Board와 똑같은 구조
    Q = deque()
    Q.append(s)
    visited[s[0]][s[1]] = 1
    while Q:
        now = Q.popleft()
        for k in range(4):
            next = (now[0] + dx[k], now[1] + dy[k])
            if next == g:
                return visited[now[0]][now[1]] - 1

            elif 0 <= next[0] < N and 0 <= next[1] < N and Board[next[0]][next[1]] == 0 and visited[next[0]][next[1]] == 0:
                Q.append((next[0], next[1]))
                visited[next[0]][next[1]] = visited[now[0]][now[1]] + 1


    return 0

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    Board = [list(map(int, input())) for _ in range(N)]

    # 시작점과 도착점을 찾자
    s = (0, 0)
    g = (0, 0)
    for i in range(N):
        for j in range(N):
            if Board[i][j] == 2:
                s = (i, j)
            elif Board[i][j] == 3:
                g = (i, j)

    print(f'#{test+1}', BFS(s, g, N))