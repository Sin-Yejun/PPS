a, b = input().split()
a = int(a)
b = int(b)
queue = [x+1 for x in range(a)]
ct = 1
index = 0
answer = []
while len(queue)!=0:
    if ct==b:
        answer.append(queue[index])
        queue.pop(index)
        index -=1
    ct += 1
    index +=1
    if index >= len(queue):
        index = 0
    if ct >= b+1:
        ct = 1

print('<',end='')
for i in answer:
    if i != answer[-1]:
        print(i,end=', ')
    else:
        print(i, end='')
print('>')
    
    
    
