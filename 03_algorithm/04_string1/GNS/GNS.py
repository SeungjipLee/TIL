import sys
sys.stdin = open("GNS_test_input.txt")

Testcase = int(input())
for test in range(Testcase):
    A, B = input().split()
    List = list(input().split())
    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    count = [0] * 10
    for i in List:
        if i == 'ZRO':
            count[0] += 1
        elif i == 'ONE':
            count[1] += 1
        elif i == 'TWO':
            count[2] += 1
        elif i == 'THR':
            count[3] += 1
        elif i == 'FOR':
            count[4] += 1
        elif i == 'FIV':
            count[5] += 1
        elif i == 'SIX':
            count[6] += 1
        elif i == 'SVN':
            count[7] += 1
        elif i == 'EGT':
            count[8] += 1
        elif i == 'NIN':
            count[9] += 1
    print(A)
    for j in range(10):
        print(f'{numbers[j]} '* count[j])