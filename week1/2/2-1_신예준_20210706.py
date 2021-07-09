string = ''
while True:
    string = input()
    if string == 'end':
        break
    vowel = ['a','e','i','o','u']
    vowel_exist = False
    flag = True
    count_v = 0
    count_c = 0
    check = False
    pv = ''
    for i in string:
        if pv == i:
            flag = False
        if i!='e' and i!='o':
            pv = i
        if i in vowel:
            count_v += 1
            count_c = 0
        else:
            count_c+=1
            count_v = 0
        if(count_v != 0):
            check = True
        if(count_v == 3 or count_c == 3):
            flag = False
        
    if flag == True:
        if(check == False):
            print('<'+string+'> is not acceptable.')
        else:
            print('<'+string+'> is acceptable.')
    else:
        print('<'+string+'> is not acceptable.')

