import sys
sys.stdin = open("input.txt")

Testcase = int(input())
for test in range(1, Testcase+1):
    N = int(input())
    count = 0
    Board = [[0]*10 for _ in range(10)]
    for n in range(N):
        x1, y1, x2, y2, c = map(int, input().split())
        if c == 1:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    Board[i][j] += 1
        else:
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    Board[i][j] += 2

    for k in range(10):
        for l in range(10):
            if Board[k][l] == 3:
                count += 1

    print(f'#{test}', count)