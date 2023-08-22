import sys
sys.stdin = open('sample_input (2).txt')

def inorder(node):
    global k
    if node != 0:
        inorder(left[node])
        info[node] = k
        k += 1
        inorder(right[node])

Testcase = int(input())
for test in range(Testcase):
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    # parent = [0] * (N+1)
    info = [0] * (N+1)
    for i in range(1, N//2+1):
        left[i] = i*2
        if i*2+1 <= N:
            right[i] = i*2+1
    k = 1
    inorder(1)
    # print(left)
    # print(right)
    # print(info)
    print(f'#{test+1}', info[1], info[N//2])
