def HanSu(n):
    s = str(n)
    for i in range(len(s)-2):
        print(s[i], s[i+1], s[i+2])
        if int(s[i+1])-int(s[i]) == int(s[i+2])-int(s[i+1]):
            print("yes")
            continue
        else:
            return 0
    return 1

HanSu(100)