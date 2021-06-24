def self_num(n):
    val = n
    for i in str(n):
        val += int(i)
    return val


num = []
for i in range(10001):
    num.append(i)
n=0
while n <10001:
    try:
        num.remove(self_num(n))
    except:
        1
    n += 1
    
for i in num:
    print(i)
