import sys
sys.stdin = open("input (4).txt")


def second(arr):
    maxx = 0
    summ = 0
    for i in range(len(arr)):
        if arr[i] >= maxx:
            maxx = arr[i]
            max_idx = i
    for j in range(max_idx):
        summ += maxx - arr[j]
    return summ, arr[max_idx + 1:]


Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    Price_list = list(map(int, input().split()))
    interest = 0
    A, B = second(Price_list)
    interest += A
    while len(B) != 1 and len(B) != 0:
        A, B = second(B)
        interest += A
    print(f'#{test + 1}', interest)
