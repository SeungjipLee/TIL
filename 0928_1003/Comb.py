arr = [1, 2, 3, 4, 5]
k = 3
temp = []
visited = [0]*5

def comb(idx):
    if len(temp) == k:
        print(*temp)
        return

    for i in range(idx, 5):
        if visited[i] == 0:
            temp.append(arr[i])
            visited[i] = 1
            comb(idx+1)
            temp.pop()
            visited[i] = 0

comb(0)