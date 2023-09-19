from math import sqrt
N = int(input())
a = (((1+sqrt(5))/2)**N-((1-sqrt(5))/2)**N)/sqrt(5)
print(int(a))

