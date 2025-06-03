a, b = list(map(int, input().split()))
n = int(input())
y = 0 #幾個人有同時購買a,b

for i in range(n): #n個人的購物車
    #一個人的購物車
    x = list(map(int, input().split())) #第i個購物車資料
    #|a| > |-a| and |b| > |-b| -> 有購買
    if x.count(a) > x.count(-a) and x.count(b) > x.count(-b):
        y += 1 #y = y+1

print(y)