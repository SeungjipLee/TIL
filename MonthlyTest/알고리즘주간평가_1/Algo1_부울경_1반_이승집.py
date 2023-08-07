import sys
sys.stdin = open("algo1_sample_in.txt")

Testcase = int(input())
for test in range(Testcase):
    # 판 크기
    N = int(input())
    # 좌표 위치
    x1,y1,x2,y2 = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    # 합과 칸 개수와 움직이는 횟수
    summ = 0
    count = 0
    move = 0
    # 순회
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            summ += Board[i][j]
            count += 1
    # 평균
    average = summ//count
    # 다시 순회하며 평균과의 차이를 더해갈 것
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            # 절댓값을 구하기 위해 case나누기
            if Board[i][j] >= average:
                move += Board[i][j] - average
            else:
                move += average - Board[i][j]

    print(f'#{test+1}', move)