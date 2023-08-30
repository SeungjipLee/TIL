import sys
sys.stdin = open("sample_input (3).txt")

Testcase = int(input())
for tc in range(Testcase):
    R = int(input())
    count = 0
    for i in range(-R, R+1):
        for j in range(-R, R+1):
            if i**2 + j**2 <= R**2:
                count += 1
    print(f'#{tc+1} {count}')