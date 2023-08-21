import sys
sys.stdin = open('input (1).txt')

def inorder(node):
    global final
    if node != 0:
        inorder(left[node])
        final += word[node]
        inorder(right[node])

for test in range(1, 11):
    V = int(input())
    word = [''] * (V+1)
    left = [0] * (V+1)
    right = [0] * (V+1)
    final = ''
    for i in range(V):
        Input = list(input().split())
        word[int(Input[0])] = Input[1]
        if len(Input) == 3:
            left[int(Input[0])] = int(Input[2])
        elif len(Input) == 4:
            left[int(Input[0])] = int(Input[2])
            right[int(Input[0])] = int(Input[3])

    inorder(1)

    print(f'#{test}', final)