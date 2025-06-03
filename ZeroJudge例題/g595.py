n = input()
h = list(map(int, input().split()))
r = 0

for i in range(len(h)):
    if h[i] == 0:
        if i == 0:
            r += h[i+1]
        elif i != len(h)-1:
            if h[i-1] > h[i+1]:
                r += h[i+1]
            else:
                r += h[i-1]
        else:
            r += h[i-1]

print(r)