k = int(input())
data = [list(map(int, input().split())) for _ in range(k)]
score = [data[i][1] for i in range(len(data))]
highest = max(score)
result = highest - k - score.count(-1) * 2
if result < 0: result = 0
for i in data:
    if i[1] == highest:
        print(result, i[0])
        break
        