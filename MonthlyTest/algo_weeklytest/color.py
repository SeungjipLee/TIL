import sys
sys.stdin = open("input.txt")

Testcase = int(input())
for test in range(1, Testcase+1):
    N = int(input())
    Board = [[0]*10 for _ in range(10)]
    count = 0
    for _ in range(N):
        x1, y1, x2, y2, c = map(int, input().split())
        if c == 1:
            for x in range(x1,x2+1):
                for y in range(y1, y2+1):
                    if Board[x][y] == 0:
                        Board[x][y] += 1
                    elif Board[x][y] == 2:
                        Board[x][y] += 1
                        count += 1
                    else:
                        pass
        else :
            for x in range(x1,x2+1):
                for y in range(y1, y2+1):
                    if Board[x][y] == 0:
                        Board[x][y] += 2
                    elif Board[x][y] == 1:
                        Board[x][y] += 2
                        count += 1
                    else:
                        pass
    print(f'#{test}', count)