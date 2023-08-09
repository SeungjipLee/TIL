import sys
sys.stdin = open('test_input.txt', encoding='utf-8')

for _ in range(10):
    tc = int(input())
    pattern = input()
    target = input()

    # 조사 대상 2개(pattern, target)의 index를 담을 변수 선언
    p_idx= 0
    t_idx = 0
    # 최종 결과값
    result = 0
    # 조사를 할건데 언제까지 반복할 것이냐
    # target의 끝까지 조사하면서, pattern이 몇번 나오는지 세야한다.
    len_target = len(target)
    while t_idx < len_target:
        # 만약 두 값이 같다면
        # if target[t_idx] == pattern[p_idx]:
        #     p_idx += 1
        #     t_idx += 1
        # else:
        #     if p_idx != 0:
        #         p_idx = 0
        #     p_idx = 0
        #     t_idx += 1
        # 로 접근하면 조건문이 까다로워진다.

        if target[t_idx] != pattern[p_idx]:
            t_idx = t_idx - p_idx
            p_idx = -1
        # t_idx 번째의 값과 p_idx 번째의 값이
        # 같거나 틀릴 때 취해야할 행동

        # 같거나 틀린 상황 이외에
        # 모든 상황에 대해서
        # p_idx와 t_idx는 증가할 것
        p_idx += 1
        t_idx += 1

        if p_idx == len(pattern):
            result += 1
            p_idx = 0

    print(f'#{tc}', result)