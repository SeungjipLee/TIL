import sys
sys.stdin = open("input.txt")

Testcase = int(input())     # 테스트케이스

for test in range(Testcase):
    # N = 리스트 길이, M = 합산 범위
    N, M = map(int, input().split())
    List = list(map(int, input().split()))
    # 이후 수정할 최대핪과 최소합 미리 언급
    max_sum = 0
    min_sum = 100*10000

    # mid_sum 중간 합
    for i in range(N-M+1):
        mid_sum = List[i]
        for k in range(1, M):
            mid_sum += List[i+k]

        # 중간 합들 중 최대 최소 선택
        if mid_sum >= max_sum:
            max_sum = mid_sum
        if mid_sum <= min_sum:
            min_sum = mid_sum
    # 차이 구하기
    div = max_sum - min_sum
    print(f'#{test+1} {div}')