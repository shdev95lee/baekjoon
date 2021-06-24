def HanSu(n):
    s = str(n)
    for i in range(len(s)-2):
        if int(s[i+1])-int(s[i]) == int(s[i+2])-int(s[i+1]):
            continue
        else:
            return 0
    return 1

n = int(input())
count =0
for i in range(n):
    if HanSu(i+1):
        count += 1
print(count)