import sys
sys.stdin = open("sample_input (2).txt")

# 팩토리얼을 그냥 구현하니 에러가 떠서
# 메모이제이션을 통해 구현하여 통과!
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
    N = int(input())//10    # 종이의 단위가 10 단위라 10으로 나누자
    memo = [0]*N
    result = 0
    count_1 = N+2   # 아래서 자연수의 분할에 나오는 1의 개수
    count_2 = -1    # 자연수 분할에서의 2의 개수를 셀 것

    '''
    자연수의 분할이란?
    예를 들어 7을 분할하면
    1) 1111111
    2) 111112
    3) 11122
    4) 1222
    로 총 4가지 큰 종류가 나온다.
    '''
    for i in range(N//2+1):
        count_1 -= 2
        count_2 += 1
        if count_2 == 0:
            result += 1
        # 이후 같은 것이 있는 순열로 경우의 수를 곱한다.
        '''
        위의 예시에서 3)의 케이스인 11122 를 보면
        같은 것이 있는 순열으로
        전체 5! 에서 3!과 2!을 나눠주면 10개의 경우의 수가 나온다.
        (1) 11122
        (2) 11212
        (3) 12112
        (4) 21112
        (5) 11221
        (6) 12121
        (7) 21121
        (8) 12211
        (9) 21211
        (10)22111
        '''

        # 2라는 길이에 올 수 있는 종류는  = 모양과 ㅁ 모양 으로 2가지 이므로
        # 2 개수만큼 2의 n제곱을 곱한다.
        # 결론 :  각 자연수 분할마다 / 같은 것이 있는 순열 곱하고 / 2 개수만큼 2의 n제곱 곱함
        else:
            result += factorial(count_1 + count_2)//(factorial(count_1)*factorial(count_2)) * (2 ** count_2)

    print(f'#{test+1}', result)



    # 50 이라는 숫자를 입력 받으면 5으로 해석해도 된다

    #  11111   -> 1개
    #  1112  1121   1211    2111 -> 같은 것이 있는 순열 4!/3!*1! * 2  -> 8개
    #   122 -> 3가지* 2**2 -> 12가지
    ㅓㅓ