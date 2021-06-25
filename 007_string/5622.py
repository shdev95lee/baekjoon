s = input()
sum =0
for a in s:
    if 'A' <= a and a <= 'C':
        sum += 2
    elif 'D' <= a and a <= 'F':
        sum += 3
    elif 'G' <= a and a <= 'I':
        sum += 4
    elif 'J' <= a and a <= 'L':
        sum += 5
    elif 'M' <= a and a <= 'O':
        sum += 6
    elif 'P' <= a and a <= 'S':
        sum += 7
    elif 'T' <= a and a <= 'V':
        sum += 8
    elif 'W' <= a and a <= 'Z':
        sum += 9
sum += len(s)
print(sum)