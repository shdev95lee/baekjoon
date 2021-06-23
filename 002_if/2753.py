i = int(input())
if i%4 != 0:
    print(0)
elif i%100 != 0:
    print(1)
elif i%400 != 0:
    print(0)
else:
    print(1)