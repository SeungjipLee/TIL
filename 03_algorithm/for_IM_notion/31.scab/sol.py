import sys
sys.stdin = open('a.txt')

N = int(input())
for _ in range(N):
    A_cnt = [0] * 5
    B_cnt = [0] * 5
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in A[1:]:
        A_cnt[i] += 1
    for i in B[1:]:
        B_cnt[i] += 1
    i = 4
    while 1:
        if A_cnt[i] > B_cnt[i]:
            print('A')
            break
        elif A_cnt[i] < B_cnt[i]:
            print('B')
            break
        else:
            if i == 0:
                print('D')
                break
            else:
                i -= 1
            continue