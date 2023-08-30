import sys
sys.stdin = open("input.txt")

Testcase = int(input())
for test in range(Testcase):
    Board = [list(map(int, input().split())) for _ in range(9)]

    # 조사 횟수
    count = 0

    # 행 조사
    for i in range(9):
        if set(Board[i]) == set(range(1, 10)):
            count += 1

    # 열 조사
    for i in range(9):
        List = []
        for j in range(9):
            List.append(Board[j][i])
            if set(List) == set(range(1, 10)):
                count += 1

    # 박스 조사
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            Li = []
            for k in range(3):
                for l in range(3):
                    Li.append(Board[i+k][j+l])
            if set(Li) == set(range(1, 10)):
                count += 1

    if count == 27:
        print(f'#{test+1}', 1)
    else:
        print(f'#{test+1}', 0)