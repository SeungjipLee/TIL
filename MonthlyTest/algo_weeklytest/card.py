Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    L = list(map(int, input()))
    C = [0]*10
    for i in L:
        C[i] += 1
    maxx = 0
    max_in = 0
    for j in range(len(C)):
        if C[j] >= maxx:
            maxx = C[j]
            max_in = j
    print(f'#{test+1}', max_in, maxx)