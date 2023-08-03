import sys
sys.stdin = open("sample_input (2).txt")

def sel_sort(arr):
    for i in range(10):
        if i%2 == 0:
            max_idx = i
            for j in range(i+1, len(arr)):
                if arr[max_idx] < arr[j]:
                    max_idx = j
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
        else:
            min_idx = i
            for j in range(i+1, len(arr)):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    List = list(map(int, input().split()))
    arr = sel_sort(List)
    print(f'#{test+1}', *arr[:10])