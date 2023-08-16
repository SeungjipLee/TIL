import sys

sys.stdin = open('sample_input.txt')

Testcase = int(input())
for test in range(Testcase):
    IN = list(input().split())
    stack = []
    final = 'error'
    for i in IN:
        if i not in '.+-*/':
            stack.append(int(i))
        else:
            if len(stack) >= 2 and i == '+':
                stack.append(stack.pop() + stack.pop())
            elif len(stack) >= 2 and i == '-':
                stack.append(-(stack.pop() - stack.pop()))
            elif len(stack) >= 2 and i == '*':
                stack.append(stack.pop() * stack.pop())
            elif len(stack) >= 2 and i == '/':
                try:
                    f = stack.pop()
                    s = stack.pop()
                    stack.append(int(s / f))
                except ZeroDivisionError:
                    break
            elif len(stack) == 1 and i == '.':
                final = stack[0]
            else:
                break
    print(f'#{test + 1}', final)
