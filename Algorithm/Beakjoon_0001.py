L = input()
sum = 0
for i in range(len(L)):
    if ord(L[i])>=87:
        s = 10
    elif ord(L[i])>=84:
        s = 9
    elif ord(L[i])>=80:
        s = 8
    elif ord(L[i])>=77:
        s = 7
    elif ord(L[i])>=74:
        s = 6
    elif ord(L[i])>=71:
        s = 5
    elif ord(L[i])>=68:
        s = 4
    else :
        s = 3
    sum += s
print(sum)