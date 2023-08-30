import sys
sys.stdin = open("input1.txt")

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    final = 0

    for i in range(N):
        for j in range(M):
            R = Board[i][j]
            compare_list = [R]
            for k in range(4):
                for l in range(1, R+1):
                    nx = i + dx[k] * l
                    ny = j + dy[k] * l
                    if (0 <= nx < N) and (0 <= ny < M):
                        compare_list.append(Board[nx][ny])
            summ = sum(compare_list)
            if final <= summ:
                final = summ
    print(f'#{test+1}', final)