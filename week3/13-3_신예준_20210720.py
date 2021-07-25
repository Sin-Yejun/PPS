import sys
n, L = input().split()
n = int(n)
L = int(L)
l = list(map(int,sys.stdin.readline().split()))
l.sort()
for i in l:
    if L >= i:
        L+=1
    else:
        break
print(L)
