for i in range(int(input())):
    s = list(map(int,input().split()))
    avg =0
    for j in range(s[0]):
        avg += s[j+1]
    avg = avg/s[0]
    over_avg =0
    for j in range(s[0]):
        if s[j+1] > avg:
            over_avg += 1
    print(str('%0.3f'%(over_avg/s[0]*100))+"%")