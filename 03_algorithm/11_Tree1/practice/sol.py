import sys
sys.stdin = open('input.txt')

# 전위 순회
def preorder(node):
    if node != 0:
        print(node, end=' ')
        preorder(left[node])
        preorder(right[node])

# 중위 순회
def inorder(node):
    if node != 0:
        inorder(left[node])
        print(node, end=' ')
        inorder(right[node])

# 후위 순회
def postorder(node):
    if node != 0:
        postorder(left[node])
        postorder(right[node])
        print(node, end=' ')


V = int(input())
E = V - 1
edge = list(map(int, input().split()))

# 왼쪽 자식, 오른쪽 자식, 부모 정보
left = [0] * (V+1)
right = [0] * (V+1)
parent = [0] * (V+1)

# 간선 정보 전수 조사
for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    parent[c] = p

root = 0
for i in range(1, V+1):
    if parent[i] == 0:
        root = i
        break
# print(root)
#
#
# print(edge)
# print(left)
# print(right)
# print(parent)
print('===전위 순회===')
preorder(root)
print()
print('===중위 순회===')
inorder(root)
print()
print('===후위 순회===')
postorder(root)