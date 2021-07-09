size = int(input())

output = 0
for n in range(size):
    string = input()
    li = []
    pv =''
    Flag = True
    for i in string:
        if i != pv and i not in li: #이전 문자와 다르고 list에 없으면
            pv = i
            li.append(i)
        if i !=pv and i in li:      #이전 문자와 다른데 list에 있으면
            Flag = False
        
    if(Flag == True):
        output +=1
print(output)
