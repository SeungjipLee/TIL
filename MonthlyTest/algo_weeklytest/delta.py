dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]

    summ = 0
    for i in range(N):
        for j in range(N):
            mid = Board[i][j]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0<=nx<N and 0<=ny<N:
                    summ+=abs(mid-Board[nx][ny])
    print(f'#{test+1}',summ)