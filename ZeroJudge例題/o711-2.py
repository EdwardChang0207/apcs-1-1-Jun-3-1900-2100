n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

v1 = a[0]**2*a[2]
v2 = a[1]**2*a[3]
v = 0
h = []

for i in range(n):
    if v + b[i] >= v1 + v2:
        if v >= v1:
            b[i] = v1+v2-v
            h.append(b[i]//a[1]**2)
        else:
            h.append((v1-v)//a[0]**2 + a[3])
    
    elif v + b[i] > v1 and v >= v1:
        h.append(b[i]//a[1]**2)

    elif v + b[i] > v1:
        h.append((v1-v) // a[0]**2 + (b[i]-(v1-v)) // a[1]**2)

    else:
        h.append(b[i]//a[0]**2)
    v += b[i]

print(max(h))