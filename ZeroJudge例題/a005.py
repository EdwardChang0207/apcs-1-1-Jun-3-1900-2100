#init input
t = int(input())
for i in range(t):
    l = list(map(int, input().split()))

#process
    if l[1]-l[0] == l[2]-l[1]:
        l.append(l[-1]+l[1]-l[0])
        #等差
    else:
        l.append(int(l[-1]*l[1]/l[0]))
        #等比

#output
    print(*l)

# [1, 2, 3, 4, 5] len = 5

# for i in s: -> 找元素

# for i in range(len(s)) -> 找位置

# range(start, end, interval) -> raneg(5)