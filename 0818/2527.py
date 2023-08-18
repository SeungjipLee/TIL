import sys

sys.stdin = open('2527.txt')

for tc in range(1, 5):
    sq_list = list(map(int, input().split()))
    s1 = set()
    s2 = set()
    for i in range(sq_list[0], sq_list[2] + 1):
        for j in range(sq_list[1], sq_list[3] + 1):
            s1.add((i, j))

    for i in range(sq_list[4], sq_list[6] + 1):
        for j in range(sq_list[5], sq_list[7] + 1):
            s2.add((i, j))

    union = list(s1 & s2)
    check_set_row = set()
    check_set_col = set()
    for i in union:
        check_set_row.add(i[0])
        check_set_col.add(i[1])

    if len(union) == 0:
        print('d')
    elif len(union) == 1:
        print('c')
    else:
        if len(check_set_row) == 1 or len(check_set_col) == 1:
            print('b')
        else:
            print('a')
