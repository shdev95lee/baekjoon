a, b = input().split()
for i in range(3):
    if a[2-i] > b[2-i]:
        for j in range(3):
            print(a[2-j], end="")
        break
    elif a[2-i] < b[2-i]:
        for j in range(3):
            print(b[2-j], end="")
        break
print()
