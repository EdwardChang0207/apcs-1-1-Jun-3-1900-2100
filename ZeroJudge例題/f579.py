a, b = map(int, input().split())
n = int(input())

buy = 0
for _ in range(n):
    cart = list(map(int, input().split()))
    if (a in cart) and (b in cart):
        if (cart.count(a) > cart.count(-1*a)) and (cart.count(b) > cart.count(-1*b)):
            buy += 1

print(buy)