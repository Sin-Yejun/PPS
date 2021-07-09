array = [ [0 for col in range(15)] for row in range(15)]

for i in range(15):
    for j in range(15):
        if i == 0:
            array[i][j] = j+1 
    array[i][0] = 1
n = int(input())
for k in range(n): 
    a = int(input())
    b = int(input())
    for i in range(1,a+1):
        for j in range(1,b+1):
            array[i][j] = array[i-1][j]+array[i][j-1]
    print(array[a][b-1])
