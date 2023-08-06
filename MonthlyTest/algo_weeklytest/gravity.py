Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    List = list(map(int, input().split()))
    count = 0

    for i in range(len(List)-1):
        mid_count = 0
        for j in List[i:]:
            if List[i] > j:
                mid_count += 1
        if mid_count > count:
            count = mid_count
    
    print(f'#{test+1}', count)