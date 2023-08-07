# 빙고(2578번)
Board = [list(map(int, input().split())) for _ in range(5)]
Host = [list(map(int, input().split())) for _ in range(5)]
ho_list = []
count = 0

for i in range(5):
    for j in range(5):
        ho_list.append(Host[i][j])

for k in range(25):
    summ = 0
    sumn = 0
    sumx1 = 0
    sumx2 = 0
    for i in range(5):
        for j in range(5):
            if Board[i][j] == ho_list[k]:
                Board[i][j] = 0
                if i == j:
                    for m in range(5):
                        sumx1 += Board[m][m]
                        summ += Board[i][m]
                        sumn += Board[m][j]
                    if sumx1 == 0:
                        count += 1
                elif i == 5-j:
                    for n in range(5):
                        sumx2 += Board[n][4-n]
                        summ += Board[i][n]
                        sumn += Board[n][j]
                else:
                    for l in range(5):
                        summ += Board[i][l]
                        sumn += Board[l][j]