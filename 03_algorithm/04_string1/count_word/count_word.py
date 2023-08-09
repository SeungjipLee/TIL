import sys
sys.stdin = open('sample_input.txt')

Testcase = int(input())
for test in range(Testcase):
    str1 = input()
    str2 = input()
    newdict = dict()
    maxx = 0

    for i in str2:
        if i not in newdict:
            newdict[i] = 1
        else:
            newdict[i] += 1

    for i in str1:
        if newdict[i] >= maxx:
            maxx = newdict[i]

    print(f'#{test+1}', maxx)