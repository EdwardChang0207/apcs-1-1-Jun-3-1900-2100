n = int(input())

x = list(map(int, input().split())) #1
y = list(map(int, input().split())) #2

for i in range(n):
    #一組對聯
    result = ''
    #A
    if not((x[1] != x[3] and x[1] == x[5]) and (y[1] != y[3] and y[1] == y[5])): #違反A
        result += 'A'
    #B
    if not(x[-1] == 1 and y[-1] == 0): #違反B
        result += 'B'
    #C
    if not(x[1] != y[1] and x[3] != y[3] and x[5] != y[5]): #違反C
        result += 'C'
    
    if result:
        print(result)
    else:
        print('None')