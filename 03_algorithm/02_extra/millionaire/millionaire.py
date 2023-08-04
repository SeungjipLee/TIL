import sys
sys.stdin = open("input (4).txt")

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    Price_list = list(map(int, input().split()))

    max_index = 0
    maximum = 0
    interest = 0

    for i in range(len(Price_list)):
        if Price_list[i] >= maximum:
            maximum = Price_list[i]
            max_index = i

    while max_index != N-1:
        if max_index != 0:
            for j in range(max_index):
                interest += abs(Price_list[j] - maximum)
            Price_list = Price_list[max_index+1:]
            maximum = Price_list[0]
            max_index = 0
            for k in range(len(Price_list)):
                if Price_list[k] >= maximum:
                    maximum = Price_list[k]
                    max_index = k
        else:
            Price_list = Price_list[1:]
            maximum = Price_list[0]
            max_index = 0
            for l in range(len(Price_list)):
                if Price_list[l] >= maximum:
                    maximum = Price_list[l]
                    max_index = l
    if (max_index == 1) and (max_index == N-1):
        interest += abs(Price_list[0] - Price_list[1])


    print(f'#{test+1}', interest)