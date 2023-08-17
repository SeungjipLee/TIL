import sys
sys.stdin = open('sample_input.txt')

Testcase = int(input())
for test in range(1, Testcase+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    compare_list = []
    for i in range(N-M+1):
        compare_list.append(sum(numbers[i:i+M]))
    print(f'#{test}', max(compare_list) - min(compare_list))