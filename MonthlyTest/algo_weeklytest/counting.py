def counting_sort(numbers, k):
    count_arr = [0]*(k+1)
    result = [-1] * len(numbers)
    for i in range(len(numbers)):
        count_arr[numbers[i]] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]

    for num in numbers:
        count_arr[num] -= 1
        result[count_arr[num]] = num
    return result

numbers = [0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(numbers, 4))