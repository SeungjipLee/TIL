# 5 개를 예를 들어 진행해보자
# 배열 [6 4 19 1 9]
List = [5,4,3,2,1]

for i in range(1, len(List)):
    for j in range(len(List)-i):
        if List[j] > List[j + 1]:
            List[j], List[j + 1] = List[j + 1], List[j]

print(List)

# for i in range(len(List)-1):
#     if List[i] > List[i+1]:
#         List[i], List[i+1] = List[i+1], List[i]
# print(List)
#
# for i in range(len(List)-2):
#     if List[i] > List[i+1]:
#         List[i], List[i+1] = List[i+1], List[i]
# print(List)
#
# for i in range(len(List)-3):
#     if List[i] > List[i+1]:
#         List[i], List[i+1] = List[i+1], List[i]
# print(List)
#
# for i in range(len(List)-4):
#     if List[i] > List[i+1]:
#         List[i], List[i+1] = List[i+1], List[i]
# print(List)