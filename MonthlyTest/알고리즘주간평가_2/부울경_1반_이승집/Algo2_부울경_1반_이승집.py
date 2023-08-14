Testcase = int(input())
for test in range(Testcase):
    String = input()
    stack = []      # 괄호의 짝이 맞는지 검사하기 위한 스택
    T_F = -1        # 최종 결과 값이 될 것

    # 시작이 괄호가 아니면 -1
    if String[0] != '(' and String[0] != '{':
        pass
    # 끝이 이상해도 -1
    if String[-1] != ')' and String[-1] != '}':
        pass
    else:
        # 괄호 짝이 맞는지 먼저 검사하자
        for i in String:
            if i == '(' or i == '{':
                stack.append(i)
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)
        if stack:
            pass

        # 괄호 상태 좋고, 양 끝에 숫자 없는 애들만 살아남음
        else:
            stack_2 = []        # 계산 결과를 찾을 스택 만들기
            for i in String:    # 순회하면서 스택에 추가
                if i != ')' and i != '}':
                    stack_2.append(i)

                elif i == ')':      # 소괄호가 닫히면 덧셈 연산을 해야하므로
                    mid = 0         # 덧셈 항등원인 0을 들고와서 숫자들 전부 더해감
                    while stack_2[-1] != '(':
                        mid += int(stack_2.pop())
                    stack_2.pop()   # 괄호 하나 빼주고
                    stack_2.append(mid) # 그 결과를 추가

                elif i == '}':      # 중괄호가 닫히면 곱셈 연산을 해야하므로
                    mid = 1         # 곱셈 항등원인 1을 들고와서 숫자들 전부 곱해감
                    while stack_2[-1] != '{':
                        mid *= int(stack_2.pop())
                    stack_2.pop()
                    stack_2.append(mid)
            T_F = stack_2[0]        # 마지막 스택에 최종적으로 남은 값이 결과가 된다.

    print(f'#{test+1}', T_F)