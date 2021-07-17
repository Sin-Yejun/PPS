import sys
# nHm-n 중복조합을 이용하여 계산
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

r = m-n
a = n+r-1
answer = 1
d = 1
for i in range(r):
    answer *= a
    a += -1
for i in range(1,r+1):
    d *= i

print(answer//d)



