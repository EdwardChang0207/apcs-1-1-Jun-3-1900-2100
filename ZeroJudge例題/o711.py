n = int(input()) #倒水次數
w1, w2, h1, h2 = map(int, input().split()) #杯子容量寬、高
water_in = list(map(int, input().split()))

v = 0 #目前裝盛裝體積
h_max = 0 #最大上升高度

for i in water_in:
    #溢出
    if v + i > w1**2*h1 + w2**2*h2:
        i = (w1**2*h1 + w2**2*h2) - v

    #第一層未裝滿且加水後不會超出第一層
    if (v + i) <= w1**2*h1:
        h = int(i / w1**2)
    #第一層未裝滿且加水後會超出第一層
    elif (v + i) > w1**2*h1 and v <= w1**2*h1:
        gap = w1**2*h1 - v
        h = int(gap / w1**2) + int((i-gap) / w2**2)
    #第一層已裝滿
    else:
        h = int(i / w2**2)
    
    v += i
    
    if h > h_max:
        h_max = h

print(h_max)