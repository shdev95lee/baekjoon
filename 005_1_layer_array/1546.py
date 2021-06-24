n = int(input())
s = list(map(int,input().split()))
avg =0
for i in s:
    avg += i
avg = avg/len(s)
s.sort()
avg = avg*100/s[len(s)-1]
print(avg)