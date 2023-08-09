def pascal(arr, n):         # n번째 줄의 원리
    if n != 2:
        new_arr = [1] * n
        for i in range(1, n - 1):
            new_arr[i] = arr[i - 1] + arr[i]
        return new_arr
    else:
        return [1, 1]

def fin_pascal(n):          # 출력
    A = [1]
    for i in range(2, n + 2):
        A = pascal(A, i)
        print(*A)
    return None


Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    print(f'#{test + 1}')
    if N != 1:
        print(1)
        fin_pascal(N-1)
    else :
        print(1)