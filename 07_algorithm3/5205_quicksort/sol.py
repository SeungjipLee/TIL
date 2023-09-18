import sys
sys.stdin = open('a.txt')

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 피벗을 중간 요소로 선택
    left = [x for x in arr if x < pivot]  # 피벗보다 작은 요소들을 모으는 리스트
    middle = [x for x in arr if x == pivot]  # 피벗과 같은 요소들을 모으는 리스트
    right = [x for x in arr if x > pivot]  # 피벗보다 큰 요소들을 모으는 리스트

    # 왼쪽, 중간, 오른쪽 부분 리스트들을 재귀적으로 정렬하고 병합
    return quick_sort(left) + middle + quick_sort(right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_list = quick_sort(arr)
    print(sorted_list)
    print(f'#{tc}',sorted_list[N//2])
