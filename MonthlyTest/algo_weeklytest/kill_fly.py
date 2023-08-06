import sys
sys.stdin = open("input(2).txt")

Testcase = int(input())
for test in range(1, Testcase+1):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    maxx = 0
    for i in range(N-M):
        for j in range(N-M):
            mid = 0
            for k in range(M):
                for l in range(M):
                    mid += Board[i+k][j+l]
            if mid >= maxx:
                maxx = mid
    print(f'#{test}', maxx)