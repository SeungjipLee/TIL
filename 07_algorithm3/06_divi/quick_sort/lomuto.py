# 특정 지점을 pivot으로 잡아서 pivot보다 큰 구간 작은 구간을 구분지음
# 배열,(중앙을 기준으로)왼쪽/오른쪽 값을 잡아놓고 시작
def quick_sort(arr, left, right):
    # 분할 정복의 가장 핵심
    # 정복 대상의 범위를 가장 작아질 때 까지 계속 쪼갠다.
    if left < right:
        mid = cal(arr, left, right)
        quick_sort(arr, left, mid - 1)
        quick_sort(arr, mid + 1, right)


# lomuto => 피봇을 가장 오른쪽 원소로 결정
def cal(arr, left, right):
    # i: 피봇보다 큰 구간의 왼쪽 경계
    i = left - 1
    # j: 피봇보다 큰 구간의 오른쪽 경계
    j = left
    pivot = arr[right]
    while j < right:
        # 피봇이 j번째 값보다 더 크면
        if pivot > arr[j]:
            i += 1
            # i와 j 사이 구간에 피봇보다 큰 값이 있다.
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                print(arr)
        j += 1
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    print(left, right)
    print(arr)
    return i + 1


nums = [23, 12, 60, 77, 32, 1]
quick_sort(nums, 0, len(nums)-1)