import sys
sys.stdin = open("input (1).txt")

Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    # 행 우선 순회
    for i in range(N):
        mid = 0
        for j in range(N):
            if board[i][j] == 1:
                mid += 1
            if j == N-1 or board[i][j] == 0:
                if mid == M:
                    count += 1
                mid = 0

    # 열 우선 순회
    for i in range(N):
        mid = 0
        for j in range(N):
            if board[j][i] == 1:
                mid += 1
            if j == N-1 or board[j][i] == 0:
                if mid == M:
                    count += 1
                mid = 0

    print(f'#{test+1}',count)