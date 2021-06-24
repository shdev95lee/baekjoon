a = []
b = []
for i in range(9):
    a.append(int(input()))
    b.append(a[i])
b.sort()
print(b[len(b)-1])
print(a.index(b[len(b)-1])+1)