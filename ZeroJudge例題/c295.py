#input
N, M = map(int, input().split())
numbers = [[int(i) for i in input().split()] for _ in range(N)]
maximum = [max(i) for i in numbers]

#process
s = sum(maximum)
pick = [i for i in maximum if s % i == 0]

#output
print(s)
if pick:
    print(*pick)
else:
    print(-1)