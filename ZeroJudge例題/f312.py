a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
n = int(input())
result = []

for i in range(0, n+1):
    y1 = a1*(n-i)**2 + b1*(n-i) + c1
    y2 = a2*i**2 + b2 * i + c2
    result.append(y1+y2)

print(max(result))