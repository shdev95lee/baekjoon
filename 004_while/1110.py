i =0
n = int(input())
a = n
while True:
    i += 1
    m = int(a/10)+a%10
    a = m%10+(a%10)*10
    if n == a:
        break
print(i)