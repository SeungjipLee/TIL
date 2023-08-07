import sys
sys.stdin = open("algo2_sample_in.txt")

Testcase = int(input())
for test in range(Testcase):
    # 판 크기와 판
    N = int(input())
    Board = list(map(int, input().split()))
    # 최종 결과의 합
    summ = 0
    # 증가량을 순회할 것
    for i in range(1, N+1):
        mid = Board[0]
        # 보폭이 배수로 늘어남
        for k in range(1, N+1):
            if (0 <= i*k < N):
                mid += Board[i*k]
        # 결과에 중간합 더하기
        summ += mid
    # 음수면 0으로
    if summ < 0 :
        summ = 0


    print(f'#{test+1}', summ)