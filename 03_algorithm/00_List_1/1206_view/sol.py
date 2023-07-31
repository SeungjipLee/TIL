import sys
sys.stdin = open("input.txt")

Testcase = 10
for test in range(Testcase):
    width = int(input())
    List = list(map(int, input().split()))
    Sum = 0

    for i in range(2, width-2):
        new_lst = [List[i-2], List[i-1], List[i], List[i+1], List[i+2]]
        max_nl = 0
        for k in new_lst:
            if k > max_nl:
                max_nl = k
        if max_nl != List[i]:
            continue
        else:
            new_lst.pop(2)
            second_max = new_lst[0]
            for j in new_lst:
                if j > second_max:
                    second_max = j
            div = max_nl - second_max
            Sum += div
    print(f'#{test+1} {Sum}')