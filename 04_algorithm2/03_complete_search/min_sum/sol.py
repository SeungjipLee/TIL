import sys
sys.stdin = open('a.txt')

dx = [0, -1]
dy = [-1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]
    final = Board[N-1][N-1]
    i = j = N-1
    while i != 0 or j != 0:
        compare = []
        for k in range(2):
            ni = i + dx[k]
            nj = j + dy[k]
            if 0<=ni and 0<=nj:
                compare.append((Board[ni][nj], ni, nj))
        if len(compare) == 1:
            i = compare[0][1]
            j = compare[0][2]
            final += compare[0][0]
        else:
            if compare[0][0] >= compare[1][0]:
                i = compare[1][1]
                j = compare[1][2]
                final += compare[1][0]
            else:
                i = compare[0][1]
                j = compare[0][2]
                final += compare[0][0]
    print(f'#{tc}', final)