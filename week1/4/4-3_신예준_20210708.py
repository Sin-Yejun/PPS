li = []
for i in range(10):
    n = int(input())
    mol = n%42
    if mol not in li:
        li.append(mol)
print(len(li))
