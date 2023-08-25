import sys
sys.stdin = open('input (3).txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]
    info = []
    decar = []

    for i in range(N):
        for j in range(N):
            if Board[i][j] != 0:
                ni = i+1
                c_ni = 1
                # 처음 0 아닌 (i, j) 를 찾음
                while Board[ni][j] != 0:
                    ni += 1
                    c_ni += 1
                nj = j+1
                c_nj = 1
                while Board[i][nj] != 0:
                    nj += 1
                    c_nj += 1
                info.append((ni, nj))
                decar.append((c_ni, c_nj))
                for l in range(c_ni):
                    for m in range(c_nj):
                        Board[i+l][j+m] = 0
            continue
    # print(decar)
    # bubble sort를 통해 곱이 큰 애들이 뒤로 가도록 하되, 같은 경우 i 인덱스가 큰 놈이 뒤로
    n = len(decar)
    for i in range(1, n):
        for j in range(n-i):
            if decar[j][0] * decar[j][1] > decar[j+1][0] * decar[j+1][1]:
                decar[j], decar[j+1] = decar[j+1], decar[j]
            elif decar[j][0] * decar[j][1] == decar[j+1][0] * decar[j+1][1]:
                if decar[j][0] > decar[j+1][0]:
                    decar[j], decar[j+1] = decar[j+1], decar[j]
    # print(decar)

    print(f'#{tc}', n, end=' ')
    for i in decar:
        print(*i, end=' ')
    print()