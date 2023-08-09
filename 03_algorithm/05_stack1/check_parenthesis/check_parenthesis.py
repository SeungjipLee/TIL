import sys
sys.stdin = open("sample_input (2).txt")

def push(item):
    global top
    if item == '(' or item == '{':
        Stack[top] = item
        top += 1
    elif item == ')':
        if Stack[top-1] == '(':
            Stack[top-1] = 0
            top -= 1
        elif top == 0:
            return False
        elif Stack[top-1] == '{':
            return False
    elif item == '}':
        if Stack[top-1] == '{':
            Stack[top - 1] = 0
            top -= 1
        elif top == 0:
            return False
        elif Stack[top-1] == '(':
            return False
    return True

Testcase = int(input())
for test in range(Testcase):
    string = input()
    N = len(string)
    Stack = [0] * N
    top = 0
    Li = []

    for i in string:
        Li.append(push(i))

    if False in Li or top != 0:
        print(f'#{test+1}', 0)
    else:
        print(f'#{test+1}', 1)