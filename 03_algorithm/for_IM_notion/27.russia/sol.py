from itertools import combinations_with_replacement
import sys
sys.stdin = open('sample_input (6).txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Board = [list(input()) for _ in range(N)]
    color = ['aW', 'bB', 'cR']
    H = list(combinations_with_replacement(color, N-3))
    # print(H)
    cnt = M*N
    A = []
    for i in H:
        A.append(list(i))
    for i in A:
        i.extend(['aW', 'bB', 'cR'])
        i.sort()
    # print(A)
    for i in A:
        for j in range(len(i)):
            i[j] = i[j][1]
    # print(A)

    # arr은 색 배열
    for arr in A:
        mid = 0
        # i번쨰 행 순회
        for i in range(N):
            for j in range(M):
                if arr[i] != Board[i][j]:
                    mid += 1
        if mid <= cnt:
            cnt = mid

    print(f'#{tc}', cnt)