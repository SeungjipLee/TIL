# 종이 자르기(2628 번)
M, N = map(int, input().split())
cutting = int(input())
width_start = 0
width_end = M
height_start = 0
height_end = N

for cut in range(cutting):
    direction, line = map(int, input().split())


    if direction == 0:
        if line >= N/2 and height_start <= line <= height_end:
            height_end = line
        elif line < N/2 and height_start <= line <= height_end :
            height_start = line

    else:
        if line >= M/2 and width_start <= line <= width_end:
            width_end = line
        elif line < M/2 and width_start <= line <= width_end:
            width_start = line

square = (width_end - width_start) * (height_end - height_start)
print(square)