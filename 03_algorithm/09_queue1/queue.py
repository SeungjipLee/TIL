from collections import deque

# queue = []
# queue.append('A')
# queue.append('B')
# print(queue.pop(0))
# print(queue)

queue = deque()
queue.append('A')
queue.append('B')
print(queue)
print(queue.popleft())
print(queue)