string = input()
for i in string:
    temp = ord(i)-3
    if(temp < 65):
        temp += 26
    print(chr(temp),end='')
    
        
