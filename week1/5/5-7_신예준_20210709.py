string = input()
li = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0
for i in li:
    if i in string:
        count += string.count(i)
        string = string.replace(i,' ')  # 가운데 글자가 없어지면 양옆이 합쳐져서 크로아티아 알파벳으로 인식될 수 있기 때문에 스페이스를 둠
string = string.replace(' ','')
print(count + len(string))
