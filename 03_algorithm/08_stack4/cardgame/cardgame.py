import sys
sys.stdin = open('sample_input (3).txt')

def logic(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        if arr[0][1] == arr[1][1]:
            return arr[0]
        elif arr[0][1] == 1:
            if arr[1][1] == 2:
                return arr[1]
            else:
                return arr[0]
        elif arr[0][1] == 2:
            if arr[1][1] == 1:
                return arr[0]
            else:
                return arr[1]
        elif arr[0][1] == 3:
            if arr[1][1] == 1:
                return arr[1]
            else:
                return arr[0]

def cut(start, end, arr):
    pivot = (start + end)//2
    left = arr[start:pivot]
    right = arr[pivot+1:]
    if len(left) <= 2 and len(right) <= 2:
        logic(left)
        logic(right)
    else:
        cut(start, pivot, left)
        cut(pivot, end, right)



Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    ran = list(range(1,N+1))
    arr = list(map(int, input().split()))
    Tu_n_p = [(ran[i], arr[i]) for i in range(N)]
    cut(1, N, Tu_n_p)