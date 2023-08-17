from collections import deque
import sys
sys.stdin = open('sample_input (5).txt')

def move():
    global M
    global N
    i = N-1
    while len(fire) != 1:
        fire.append(fire.popleft())
        cheeze[fire[-1]] //= 2
        if cheeze[fire[-1]] == 0:
            if i != M-1:
                i += 1
                fire.pop()
                fire.append(i)
            else:
                fire.pop()

    return fire[0]


Testcase = int(input())
for test in range(1, Testcase+1):
    # N : 화덕 자리 수 / M : 피자 개수
    N, M = map(int, input().split())
    cheeze = list(map(int, input().split()))
    # 화덕 만들기
    fire = deque(range(N))

    print(f'#{test}', move() + 1)