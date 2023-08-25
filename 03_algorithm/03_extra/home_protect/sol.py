import sys

sys.stdin = open('sample_input (1).txt')

Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split()) # 판 크기 N 와 한 집이 지불할 수 있는 금액 M
    Board = [list(map(int, input().split())) for _ in range(N)]
    final = 0   # 조건을 만족하는 최대 많은 집을 기록할 것
    K = 1
    while K != 2*N:
        # 보드를 순회하며 K에 따른 범위 확인
        for i in range(N):
            for j in range(N):
                # 범위 안의 집 개수를 셀 것
                mid = 0
                # 어떤 점을 기준으로 확인할 범위 로직으로 집 개수 세기
                for n in range(-K+1, 0):
                    for m in range(-K-n+1, K+n):
                        if 0 <= i + n < N and 0 <= j + m < N:
                            mid += Board[i + n][j + m]
                for n in range(1, K):
                    for m in range(-K+n+1, K-n):
                        if 0 <= i + n < N and 0 <= j + m < N:
                            mid += Board[i + n][j + m]
                # 집 개수 세기가 마무리 된 후 비용이 손해가 아닌지 확인 후 최댓값이면 final에 기록
                if mid * M - (K * K + (K - 1) * (K - 1)) >= 0:
                    if mid >= final:
                        final = mid
        # 보는 범위 1씩 증가
        K += 1

    print(f'#{test+1}', final)
