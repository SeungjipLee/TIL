import sys
sys.stdin = open('input (2).txt')

for tc in range(1, 11):
    N = int(input())
    Board = [list(input()) for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            mid = 0
            for k in range(N//2):
                if Board[i][j+k] == Board[i][j+N-k-1]:
                    mid += 1
            if mid == N//2:
                cnt += 1

    for i in range(8):
        for j in range(8-N+1):
            mid = 0
            for k in range(N//2):
                if Board[j+k][i] == Board[j+N-k-1][i]:
                    mid += 1
            if mid == N//2:
                cnt += 1

    print(f'#{tc}', cnt)