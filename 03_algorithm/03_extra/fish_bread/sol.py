import sys
sys.stdin = open('input.txt')

Testcase = int(input())
for test in range(Testcase):
    N, M, K = map(int, input().split())
    N_list = list(map(int, input().split()))
    N_list.sort()
    bread = 0
    check = 'Possible'
    for i in range(len(N_list)):
        if (N_list[i]//M) * K < i+1:
            check = 'Impossible'
            break
    print(f'#{test+1}', check)