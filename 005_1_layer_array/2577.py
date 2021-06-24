a = int(input())
b = int(input())
c = int(input())

n = str(a*b*c)
num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10):
    for j in n:
        if int(j) == i:
            num[i] += 1

for i in num:
    print(i)