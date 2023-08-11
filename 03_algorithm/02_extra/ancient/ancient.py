import sys

sys.stdin = open("input1.txt")

Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    # 행렬과 전치행렬
    Board = [list(map(int, input().split())) for _ in range(N)]

    maximum = 0

    for i in range(N):
        mid = 0
        for j in Board[i]:
            if j == 1:
                mid += 1
            else:
                if mid >= maximum:
                    maximum = mid
                mid = 0
        if mid >= maximum:
            maximum = mid

    for i in range(M):
        mid = 0
        for j in range(N):
            if Board[j][i] == 1:
                mid += 1
            else:
                if mid >= maximum:
                    maximum = mid
                mid = 0
        if mid >= maximum:
            maximum = mid
    print(f'#{test+1}', maximum)