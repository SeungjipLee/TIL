# 부분집합의 합 문제
numbers = [-7, -3, -2, 5, 8]
N = 5

# numbers로 만들 수 있는 모든 경우의 수
# 1<<N == 2**N
for x in range(1<<5):
    result = 0
    # 그 모든 경우의 수에서,
    # numbers의 y번째 요소가
    # x번 경우의 수에 사용되었는지를 판별
    # x번 경우의 수가 1일 때, bit -> 00001
    # numbers의 y번째 요소(0번째 요소) -> (1<<y)
    # numbers의 0번째 요소가 00001 -> (1<<0)
    # numbers의 1번째 요소가 00010 -> (1<<1)
    # numbers의 2번째 요소가 00011 -> (1<<2)
    for y in range(N):
        if x & (1<<y):
            result += numbers[y]
    if result == 0:
        print(1)
        break