import sys
sys.stdin = open("sample_input.txt")

Testcase = int(input())
for test in range(Testcase):
    str1 = input()
    str2 = input()
    N = len(str1)
    count = 0
    for i in range(len(str2)):
        if str1 == str2[i:i+N] and count == 0:
            count += 1
    print(f'#{test+1}', count)