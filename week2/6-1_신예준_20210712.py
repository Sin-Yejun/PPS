from collections import deque
d = deque([x+1 for x in range(int(input()))])

while len(d)!=1:
    d.popleft()
    if len(d)==1:
        break
    d.append(d[0])
    d.popleft()
print(d[0])
