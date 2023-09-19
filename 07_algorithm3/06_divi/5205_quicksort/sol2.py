import sys
sys.stdin = open('a.txt')

def quick_sort(arr):
    # 분할
    if len(arr) <= 1:
        return arr
    else:
        # 분할 작업
        pivot = arr[0]
        left, pivot_list, right = [], [pivot], []
        for i in arr:
            if i > pivot:
                right.append(i)
            elif i == pivot:
                pivot_list.append(i)
            else:
                left.append(i)
        return quick_sort(left) + [pivot] + quick_sort(right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_list = quick_sort(arr)
    print(f'#{tc}',sorted_list[N//2])