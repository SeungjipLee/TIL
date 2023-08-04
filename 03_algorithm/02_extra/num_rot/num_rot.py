import sys
sys.stdin = open("input (6).txt")

def rot_90(arr, N):
    New_list = []
    for i in range(N):
        nsmall_List = []
        for j in range(N):
            nsmall_List.append(arr[N-1-j][i])
        New_list.append(nsmall_List)
    return New_list

Testcase = int(input())
for tc in range(1, Testcase + 1):
    Mat_size = int(input())
    Board = [list(map(int, input().split())) for _ in range(Mat_size)]

    rot_1 = rot_90(Board, Mat_size)
    rot_2 = rot_90(rot_1, Mat_size)
    rot_3 = rot_90(rot_2, Mat_size)

    print(f'#{tc}')
    for i in range(Mat_size):
        print(*rot_1[i], sep='', end=' ')
        print(*rot_2[i], sep='', end=' ')
        print(*rot_3[i], sep='')