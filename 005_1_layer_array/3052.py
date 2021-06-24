a = []
for i in range(10):
    a.append(int(input()))
b=[]
for i in a:
    b.append(i%42)

c=[]
for i in b:
    if i not in c:
        c.append(i)

print(len(c))