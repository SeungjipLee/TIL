import sys
sys.stdin = open('input (1).txt')

Testcase = 10
for test in range(Testcase):
    N = int(input())
    sentence = input()
    stack = []
    st_sen = ''
    for i in sentence:
        if i == '(':
            stack.append(i)
        elif i in '*/':
            while stack and stack[-1] in '*/':
                st_sen += stack.pop()
            stack.append(i)
        elif i in '+-':
            while stack and stack[-1] != '(':
                st_sen += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                st_sen += stack.pop()
            stack.pop()
        else:
            st_sen += i

    while stack:
        st_sen += stack.pop()

    # print(st_sen, stack)

    cal_stack = []
    for i in st_sen:
        if i == '+':
            cal_stack.append(cal_stack.pop()+cal_stack.pop())
        elif i == '-':
            cal_stack.append(-(cal_stack.pop() - cal_stack.pop()))
        elif i == '*':
            cal_stack.append(cal_stack.pop() * cal_stack.pop())
        elif i == '/':
            a = cal_stack.pop()
            b = cal_stack.pop()
            cal_stack.append(b//a)
        else:
            cal_stack.append(int(i))
    print(f'#{test+1}',cal_stack[0])