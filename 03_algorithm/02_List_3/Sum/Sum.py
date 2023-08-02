import sys
sys.stdin = open("input (1).txt")

Testcase = 10
for _ in range(Testcase):
    test = int(input())
    List = [list(map(int,input().split())) for _ in range(100)]
    # print(List)
    compare_list = []
    # 행의 합
    for i in range(100):
        compare_list.append(sum(List[i]))

    # 열의 합
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += List[j][i]
        compare_list.append(row_sum)

    # 대각선의 합 - 1
    sum_1 = 0
    for i in range(100):
        sum_1 += List[i][i]
    compare_list.append(sum_1)

    # 대각선의 합 - 2
    sum_2 = 0
    for i in range(100):
        sum_2 += List[99-i][i]
    compare_list.append(sum_2)

    result = max(compare_list)

    print(f'#{test} {result}')