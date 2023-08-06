def BubbleSort(arr, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

List = [4, 13, 26, 3, 0, 511]
print(BubbleSort(List, len(List)))