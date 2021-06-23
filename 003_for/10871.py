a, n = map(int, input().split())
m = list(map(int,input().split()))
out = []
for i in m:
    if i < n:
        out.append(i)
for i in range(len(out)):
    if i != len(out)-1:
        print(out[i], end=" ")
    else:
        print(out[i])