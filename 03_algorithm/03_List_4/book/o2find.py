import sys
sys.stdin = open("sample_input (2).txt")


def binary_search(arr, N, key):
    start = 0
    end = N-1
    count = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == key:
            count += 1
            return count

        elif arr[mid] > key:
            end = mid
            count += 1

        else:
            start = mid
            count += 1
    return count

Testcase = int(input())
for tc in range(Testcase):
    Max, A_goal, B_goal = map(int, input().split())
    Book = list(range(1, Max + 1))
    AA = binary_search(Book,Max,A_goal)
    BB = binary_search(Book,Max,B_goal)
    if AA > BB:
        print(f'#{tc+1} B')
    elif AA < BB:
        print(f'#{tc+1} A')
    else:
        print(f'#{tc+1}', 0)