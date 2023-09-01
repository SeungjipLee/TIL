def DFS(idx, cnt):
    global answer
    if cnt == change:
        answer = max(int(''.join(data)), answer)
        return
    for cur in range(idx, length):
        for i in range(cur + 1, length):
            if data[cur] <= data[i]:
                data[cur], data[i] = data[i], data[cur]
                DFS(cur, cnt + 1)
                data[cur], data[i] = data[i], data[cur]

    if answer == 0 and cnt < change:
        tmp = (change - cnt) % 2
        if tmp == 1:
            data[-1], data[-2] = data[-2], data[-1]
        DFS(idx, change)


T = int(input())
for t in range(1, T + 1):
    data, change = list(map(str, input().split()))
    data = list(data)
    change = int(change)
    length = len(data)
    answer = 0
    DFS(0, 0)
    print(f'#{t} {answer}')