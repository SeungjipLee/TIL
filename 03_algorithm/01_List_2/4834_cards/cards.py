import sys
sys.stdin = open("input.txt")

Testcase = int(input())
for i in range(Testcase):
    total = int(input())
    number = input()
    number_list = []
    for j in number:
        number_list.append(j)
    number_list = list(map(int, number_list))


    # List 의 최댓값 구하기
    maximum = 0
    for k in number_list:
        if k > maximum:
            maximum = k


    # 각 숫자의 개수 세는 리스트 만들기
    count_list = [0] * 10
    for index in number_list:
        count_list[index] += 1


    # 개수 최댓값 찾기( q 번째에서 최댓값 m 을 가진다)
    m = 0
    q = 0
    for n in range(10):
        if count_list[n] >= m:
            m = count_list[n]
            q = n

    print(f'#{i+1} {q} {m}')