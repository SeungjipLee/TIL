import sys
sys.stdin = open("sample_input (2).txt")

def push(item):
    global top
    top += 1
    if top >= 1:
        if Stack[top-1] != item:
            Stack[top] = item
        else:
            top -= 2
    else :
        Stack[top] = item

Testcase = int(input())
for test in range(Testcase):
    string = input()
    size = len(string)
    Stack = [0] * size
    top = -1
    for i in string:
        push(i)
    print(f'#{test+1}',top+1)