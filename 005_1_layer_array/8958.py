n = int(input())
for i in range(n):
    result = input()
    score =0
    continuity =0
    for j in result:
        if j == 'X':
            continuity = 0
            score += continuity
        else:
            continuity += 1
            score += continuity
    print(score)
        