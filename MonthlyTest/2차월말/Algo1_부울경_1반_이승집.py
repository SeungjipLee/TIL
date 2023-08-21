# 델타 탐색
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]     # 판 숫자 입력
    # 최대와 최소를 기록할 것
    maximum = 0
    minimum = 10*N**2
    # 각 점마다 순회하며 가장 중간 점을 기준으로 델타 탐색
    for i in range(N):
        for j in range(N):
            mid = Board[i][j]   # 중앙의 값 이후 중간합 역할
            R = Board[i][j]     # 범위 확인
            for k in range(4):
                for l in range(1, R+1):
                    ni = i + l * di[k]
                    nj = j + l * dj[k]
                    if 0 <= ni < N and 0 <= nj < N:
                        mid += Board[ni][nj]
            # 최대 최소 찾기
            if mid >= maximum:
                maximum = mid
            if mid <= minimum:
                minimum = mid
    print(f'#{test+1}', maximum - minimum)