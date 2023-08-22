import sys
sys.stdin = open('sample_input (1).txt')

def preorder(n):
    global cnt
    if n != 0:
        cnt += 1
        preorder(left[n])
        preorder(right[n])

Testcase = int(input())
for test in range(Testcase):
    E, N = map(int, input().split())
    connection = list(map(int, input().split()))
    left = [0] * (E+2)
    right = [0] * (E+2)
    parent = [0] * (E+2)
    for i in range(E):
        if left[connection[2*i]] == 0:
            left[connection[2*i]] = connection[2*i+1]
        else:
            right[connection[2*i]] = connection[2*i+1]
        parent[connection[2*i+1]] = connection[2*i]

    # print(left)
    # print(right)
    # print(parent)
    cnt = 0
    preorder(N)
    print(f'#{test+1}', cnt)