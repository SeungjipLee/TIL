from pprint import pprint
import sys

sys.stdin = open("input (1).txt")

Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    final = 0
    for i in range(N - M + 1):
        for j in range(N):
            count = 0
            center = board[i][j]
            for k in range(M):
                if (0 <= j + k < N):
                    if board[i][j+k] == 1:
                        count += 1
            if board[i][M] == 1:
                count -= 100
            if count == M:
                final += 1
    print(final)