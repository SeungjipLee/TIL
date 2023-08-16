import sys
sys.stdin = open('sample_input (1).txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    Board = [list(map(int, input())) for _ in range(N)]
    final = 0
    start = 0, 0
    goal = 0, 0
    for i in range(N):
        for j in range(N):
            if Board[i][j] == 2:
                start = i, j
            elif Board[i][j] == 3:
                goal = i, j

    # 지나갈 경로를 담을 스택 => 결국 막히면 돌아와야하니까
    path_stack = [start]
    while path_stack:
        now = path_stack.pop()
        i, j = now
        for k in range(4):
            di = i + dx[k]
            dj = j + dy[k]
            if (0 <= di < N) and (0 <= dj < N) and Board[di][dj] == 0:
                Board[di][dj] = 1
                path_stack.append((di, dj))
            elif (0 <= di < N) and (0 <= dj < N) and Board[di][dj] == 3:
                final = 1
                break


    print(f'#{test+1}', final)