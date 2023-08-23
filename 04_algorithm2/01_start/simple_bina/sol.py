import sys

sys.stdin = open('input (1).txt')

Code = {
    '3211': 0, '2221': 1, '2122': 2, '1411': 3, '1132': 4,
    '1231': 5, '1114': 6, '1312': 7, '1213': 8, '3112': 9,
}


def trans(arr):
    mid = ''
    count = 1
    for i in range(6):
        if arr[i] == arr[i + 1]:
            count += 1
        else:
            mid += str(count)
            count = 1
    mid += str(count)
    return mid


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Board = []
    for _ in range(N):
        In = input().replace('0' * M, '')
        if In != '':
            Board.append(In)
    # print(Board)

    start = []

    for j in range(M - 7):
        check = Board[0][j:j + 7]
        if trans(check) in Code:
            start.append(j)
    # print(start)

    for i in range(len(start)):
        for j in range(8):
            if start[i] + 7 * j not in start:
                start[i] = 100

    s = min(start)

    Board_1 = Board[0][s:s + 56]
    final_list = []
    for i in range(8):
        final_list.append(Code[trans(Board_1[7 * i:7 * (i + 1)])])
    # print(final_list)
    final = 0
    for i in range(8):
        if i % 2:
            final += final_list[i]
        else:
            final += final_list[i] * 3
    if final % 10 != 0:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', sum(final_list))