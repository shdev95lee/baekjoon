s = input()
s = s.upper()
num = []
for i in range(65, 91):
    count =0
    for j in s:
        if chr(i) == j:
            count +=1
    num.append(count)
n_max = max(num)
a = 0
for i in num:
    if n_max == i:
        if a == 0:
            a =1
        else:
            print("?")
            n_max = -1
            break
if n_max != -1:
    print(chr(num.index(n_max)+65))

