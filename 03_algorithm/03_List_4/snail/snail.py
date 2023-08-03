import sys
sys.stdin = open("input (3).txt")

dx = [0, 1, 0, -1]          # 델타 탐색 순서 고정(달팽이 회전 방향)
dy = [1, 0, -1, 0]

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    Numbers = list(range(1, N ** 2 + 1))  # 1~25
    Board = [[0] * N for _ in range(N)] # 전부 0을 채워 넣기
    rot = 0 # 회전입니다
    ni = 0  # 현재 위치
    nj = -1 # 현재 위치

    for i in range(len(Numbers)):
        ni += dx[rot%4]     # 현재 위치의 계속된 이동
        nj += dy[rot%4]
        if (0 <= ni < N) and (0 <= nj < N):
            if Board[ni][nj] == 0:
                Board[ni][nj] += Numbers[i]
            else:
                ni += dx[rot % 4 - 2]
                nj += dy[rot % 4 - 2]
                rot += 1
                ni += dx[rot % 4]
                nj += dy[rot % 4]
                Board[ni][nj] += Numbers[i]
        else:
            if ni >= N:
                ni -= 1
                rot += 1

            elif nj >= N:
                nj -= 1
                rot += 1

            elif ni < 0:
                ni += 1
                rot += 1

            else:
                nj += 1
                rot += 1

            ni += dx[rot % 4]
            nj += dy[rot % 4]
            Board[ni][nj] += Numbers[i]

    print(f'#{test+1}')
    for m in range(N):
        print(*Board[m])