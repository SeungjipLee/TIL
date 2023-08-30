import sys
sys.stdin = open('a.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        Board[i][0] += Board[i-1][0]
        Board[0][i] += Board[0][i-1]
    for i in range(1, N):
        for j in range(1, N):
            Board[i][j] += min(Board[i-1][j], Board[i][j-1])
    print(f'#{tc}', Board[N-1][N-1])