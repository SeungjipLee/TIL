import sys
sys.stdin = open("sample_input (2).txt")

A = list(range(1, 13))

Testcase = int(input())
for i in range(Testcase):
    N, Sum = map(int, input().split())
    mini = sum(A[:N])
    maxi = sum(A[:-N-1:-1])
    if (Sum < mini) or (Sum > maxi):
        print(f'#{i+1} 0')

    else:
        total = 0
        for x in range(1<<12):
            result = 0
            count = 0
            for y in range(12):
                if x & (1<<y):
                    result += y+1
                    count += 1
            if (result == Sum) and (count == N) :
                total += 1

        print(f'#{i+1} {total}')