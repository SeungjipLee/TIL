score_list = [77, 14, 80, 42, 59, 76, 100, 23]

def min_score(L):
    m = L[0]
    for i in L:
        if i <= m:
            m = i
    return m

print(min_score(score_list))

def under_60(L):
    count = 0
    for score in L:
        if score < 60:
            count += 1
    return count

print(under_60(score_list))


