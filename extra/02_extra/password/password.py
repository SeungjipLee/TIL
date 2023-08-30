import sys
sys.stdin = open("input (4).txt")

Testcase = 10
for test in range(Testcase):
    N, string = input().split()
    N = int(N)
    List = [_ for _ in string]


    for j in range(1,50):
        for i in range(N-2*j+1):
            if List[i] == List[i+1]:
                List.pop(i)
                List.pop(i)
                break

    st = ''
    for k in List:
        st += k
    final = int(st)
    print(f'#{test+1}', final)

    # for i in range(N-2):
    #     if List[i] == List[i+1]:
    #         List.pop(i)
    #         List.pop(i)
    #         break
    #
    # print(List)
    #
    # for i in range(N-4):
    #     if List[i] == List[i+1]:
    #         List.pop(i)
    #         List.pop(i)
    #         break
    # print(List)
    #
    # for i in range(N-6):
    #     if List[i] == List[i+1]:
    #         List.pop(i)
    #         List.pop(i)
    #         break
    # print(List)
    #
    # for i in range(N-8):
    #     if List[i] == List[i+1]:
    #         List.pop(i)
    #         List.pop(i)
    #         break
    # print(List)
