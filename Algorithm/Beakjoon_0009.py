TC = int(input())
for i in list(range(TC)):
    Word_List = list(input().split())
    for j in Word_List:
        print(j[::-1], end =' ')