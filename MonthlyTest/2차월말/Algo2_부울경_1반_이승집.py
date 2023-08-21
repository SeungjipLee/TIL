Testcase = int(input())
for test in range(Testcase):
    N, M = map(int, input().split())    # 카드 개수와 순서 입력받기
    A = list(input().split())       # A 카드덱 정보 입력 받기
    B_queue = []    # 홀수만 담는 큐
    C_stack = []    # 짝수만 담는 스택
    bonus = 0       # '+'를 만나면 1증가할 보너스
    for i in A:     # A 카드덱에서 하나씩 뽑아서
        if i == '+':    # '+'면 보너스에 1 더해질 것
            bonus += 1
        else:       # 숫자인 경우 보너스와 더해 홀수/ 짝수에 따라 B와 C 카드덱에 삽입
            if (int(i) + bonus) % 2 == 1:
                B_queue.append(int(i) + bonus)
            else:
                C_stack.append(int(i) + bonus)

    # B 카드덱에서는 M 번째를 말하면 되는데 만약 비었다면 0으로 계산
    try:
        B = B_queue[M-1]
    except IndexError:
        B = 0

    # C 카드덱에서는 뒤에서 M 번째를 말하면 되는데 만약 비었다면 0으로 계산
    try:
        for i in range(M):
            C = C_stack.pop()
    except IndexError:
        C = 0

    # B와 C 카드덱에서 뽑은 숫자를 더해서 최종 점수를 얻는다.
    print(f'#{test+1}', B + C)