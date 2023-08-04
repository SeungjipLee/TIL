import sys
sys.stdin = open("input (3).txt")

Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    final = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            mid = 0
            for k in range(M):
                for l in range(M):
                    mid += Board[i+k][j+l]
            if mid >= final:
                final = mid
    print(f'#{test+1}', final)