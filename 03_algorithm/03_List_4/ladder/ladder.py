import sys
sys.stdin = open("input (3).txt")

dx = [0, 0, -1]     # 왼쪽(0) / 오른쪽(1) / 상승(-1)
dy = [-1, 1, 0]
Testcase = 10
for _ in range(Testcase):
    test = int(input())
    Board = [list(map(int, input().split())) for _ in range(100)]
    nx = 99
    ny = 0

    for i in range(100):
        if Board[99][i] == 2:
            ny = i

    # 사실 얼마나 걸리고 얼마나 동작할지 모르니 while문으로 작성(while x != 0:)
    while nx != 0:
        for i in range(3):
            px = nx + dx[i]
            py = ny + dy[i]
            if (0 <= px < 100) and (0 <= py < 100) and (Board[px][py] == 1):
                Board[nx][ny] = 0
                nx = px
                ny = py
    print(f'#{test}', ny)