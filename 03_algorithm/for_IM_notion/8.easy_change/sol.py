import sys
sys.stdin = open('a.txt')

Testcase = int(input())
for test in range(1, Testcase+1):
    N = int(input())
    mny_unt = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt_list = [0] * 8
    for i in range(8):
        cnt_list[i] = N//mny_unt[i]
        N = N - mny_unt[i] * cnt_list[i]

    print(f'#{test}')
    print(*cnt_list)