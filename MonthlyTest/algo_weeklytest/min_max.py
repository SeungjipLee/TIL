Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    Li = list(map(int, input().split()))
    maxx = Li[0]
    minn = Li[0]
    for i in Li:
        if i >= maxx:
            maxx = i
        elif i <= minn:
            minn = i
    print(f'#{test+1}', maxx - minn)