import sys
sys.stdin = open("input (3).txt")

def palindrome(arr, N):
    count = 0
    for i in range(8-N+1):  # 다섯번 시행할거다
        mid = 0
        for k in range(N//2):  # 매번마다 N//2 번 만큼을 비교할 것이며
            if arr[i+k] == arr[N-1+i-k]:  # 그들의 인덱스의 합의 규칙은 N-1+2*i 이다.
                mid += 1
        if mid == N//2:
            count += 1
    return count

Testcase = 10
for test in range(Testcase):
    N = int(input())
    Board = [list(input()) for _ in range(8)]
    result = 0
    for i in range(8):
        result += palindrome(Board[i], N)

    for i in range(8):
        arr = []
        for j in range(8):
            arr.append(Board[j][i])
        result += palindrome(arr, N)

    print(f'#{test+1}', result)