arr = [1, 2, 3, 4, 5]
k = 3
temp = []
visited = [0]*5

def perm():
    if len(temp) == k:
        print(*temp)
        return

    for i in range(5):
        if visited[i] == 0:
            visited[i] = 1
            temp.append(arr[i])
            perm()
            visited[i] = 0
            temp.pop()

perm()