Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())
    Li = list(map(int, input().split()))

    maxi = 0
    mini = 100*10000

    for i in range(N-M+1):
        mid_sum = 0
        for j in range(M):
            mid_sum += Li[i+j]
        if mid_sum >= maxi:
            maxi = mid_sum
        elif mid_sum <= mini:
            mini = mid_sum
        
    div = maxi - mini
    print(f'#{test+1}', div)