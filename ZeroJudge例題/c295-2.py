N, M = map(int, input().split())
s = []
k = []
for i in range(N):
    r = list(map(int, input().split()))
    s.append(max(r))

print(sum(s))

for i in s:
    if sum(s) % i == 0:
        k.append(i)

if k:
    print(*k)
else:
    print(-1)