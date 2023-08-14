# 1874번 스택수열
N = int(input())
stack = []
List = []
visited = [0]*(N+1)
for i in range(N):
    List.append(int(input()))
print(List)
for i in List:
    k = 0
    while len(stack) != i-k:
        if len(stack) < i:
            stack.append('+')
            print('+')
        elif len(stack) > i:
            stack.pop()
            print('-')
    stack.pop()
    print('-')
    k += 1