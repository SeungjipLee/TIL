import sys
sys.stdin = open('input.txt')

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    List = list(map(int,input().split()))
    maximum = List[0]
    minimum = List[0]
    for num in List:
        if num >= maximum:
            maximum = num
        if num <= minimum:
            minimum = num
    result = maximum - minimum
    print(f'#{test+1} {result}')