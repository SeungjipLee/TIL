import sys
sys.stdin = open("input.txt")

Testcase = int(input())
# K : 충전시 최대 이동 거리
# N : 총 거리 (0에서 출발 N이 도착)
# M : 충전기 대수
# ESL : 충전기 위치 리스트
# Count : 최종 결과 값 안되면 0 나와야함
# Site : 현재 위치
for i in range(Testcase):
    K, N, M = map(int, input().split())
    ESL = list(map(int, input().split()))
    ESL.append(N)
    Count = 0
    Site = 0

    while Site != N:
        A = []
        for j in ESL:
            if (j > Site) and (j <= Site + K):
                A.append(j)

        try:
            Count += 1
            Site = A[-1]
        except IndexError:
            Count = 0
            break

    if Count != 0:
        print(f'#{i+1} {Count-1}')
    else:
        print(f'#{i+1} 0')