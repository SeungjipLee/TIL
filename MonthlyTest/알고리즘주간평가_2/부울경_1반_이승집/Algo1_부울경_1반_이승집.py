# 델타 탐색(방향은 우 하 좌 상)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

Testcase = int(input())
for test in range(Testcase):
    # 판의 크기와 판의 정보를 입력 받는다.
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]

    # 봉오리 개수
    count = 0

    # 판의 모든 수를 순회하며 주변 값들이 자신보다 작으면 봉우리(같아도 안됨)
    for i in range(N):
        for j in range(N):
            # 기준 값은 중앙이며 비교할 대상을 리스트로 담는다.
            center = Board[i][j]
            compare = []
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 가장자리 값들은 범위 안에만 비교하면 된다.
                if (0 <= ni < N) and (0 <= nj < N):
                    compare.append(Board[ni][nj])
            # 비교 리스트를 순회하며 비교를 시작
            for idx in range(len(compare)):
                # 중앙값이 크면 True 아니면 False
                if center > compare[idx]:
                    compare[idx] = True
                else:
                    compare[idx] = False
            # 만약 거짓이 하나라도 있으면 봉오리가 될 수 없다.
            if False in compare:
                continue
            else:
                count += 1

    print(f'#{test+1}', count)