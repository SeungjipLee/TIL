Testcase = int(input())
for test in range(Testcase):
    K, N, M = map(int, input().split())
    gas_station = list(map(int, input().split()))
    site = 0
    gas_station.append(N)
    count = 0

    while site != N:
        for i in gas_station:
            mid_list = []
            if site < i <= site + K:
                mid_list.append(i)
        if len(mid_list) == 0:
            print(f'#{test+1}', 0)
            break
        else :
            mid_list.sort()
            site = mid_list[-1]
            count += 1
    print(f'#{test+1}', count)