import sys
sys.stdin = open('a.txt')

# 리스트를 반으로 나누는 함수
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 리스트를 반으로 나누기
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 재귀적으로 하위 리스트를 정렬
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # 정렬된 두 리스트를 병합
    return merge(left_half, right_half)

def merge(left, right):
    global cnt
    result = []
    left_idx, right_idx = 0, 0

    # 두 리스트를 비교하면서 작은 값을 결과 리스트에 추가
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left[-1] > right[-1]:
        cnt += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    arr = list(map(int, input().split()))
    sorted_list = merge_sort(arr)
    # print(sorted_list)
    print(f'#{tc} {sorted_list[N//2]} {cnt}')