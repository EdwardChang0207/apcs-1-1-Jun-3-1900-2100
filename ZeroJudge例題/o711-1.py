#倒水次數 n(int)
n = int(input())
#杯子尺寸 w1,w2,h1,h2
w1, w2, h1, h2 = map(int, input().split())
#倒入水量
water_in = list(map(int, input().split()))

#總體積,最大高度變化
v, h_max = 0, 0

for i in water_in: #i:每次倒入水量(int)
    if i > (w1**2*h1+w2**2*h2) - v:
        i = (w1**2*h1+w2**2*h2) - v
    if v >= w1**2*h1:
        h = int(i/w2**2)#本次的水高變化
    elif v+i > w1**2*h1:
        gap = w1**2*h1 - v
        h = int(gap / w1**2 + (i-gap) / w2**2)
    else:
        h = int(i/w1**2)
    v += i
    if h > h_max:
        h_max = h
#輸出結果
print(h_max)