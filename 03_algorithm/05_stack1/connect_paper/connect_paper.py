import sys
sys.stdin = open("sample_input (2).txt")

def factorial(n):
    global memo
    if n == 0:
        memo[0] = 1
        return memo[0]
    else:
        memo[n] = n*factorial(n-1)
        return memo[n]

Testcase = int(input())
for test in range(Testcase):
    N = int(input())//10
    memo = [0]*N
    result = 0
    count_1 = N+2
    count_2 = -1
    for i in range(N//2+1):
        count_1 -= 2
        count_2 += 1
        if count_2 == 0:
            result += 1
        else:
            result += factorial(count_1 + count_2)//(factorial(count_1)*factorial(count_2)) * (2 ** count_2)

    print(f'#{test+1}', result)