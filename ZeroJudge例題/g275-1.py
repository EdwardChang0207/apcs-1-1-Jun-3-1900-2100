n = int(input())
for i in range(n):
    a = list(map(int,input().split())) #first line
    b = list(map(int,input().split())) #second line
    r = ''

    #A
    if ((a[1] == a[3]) or (a[1] != a[5])) or ((b[1] == b[3]) or (b[1] != b[5])):#違反了A
        r += 'A'
    #B
    if (a[-1] != 1 ) or (b[-1] != 0):#違反了B
        r += 'B' 
    #C
    if  (a[1] == b[1]) or (a[3] == b[3]) or (a[5] == b[5]):#違反了C
        r += 'C'

    if r: print(r)
    else: print('None')
# ----------------------------------------------------------------------------------
n=int(input())

x=list(map(int,input().split()))
y=list(map(int,input().split()))

for i in range(n):
    if (x[1]==x[3] or y[1]==y[3] or x[1]!=x[5] or y[1]!=y[5]):
        print('A', end='')
    if (x[6]!=1 or y[6]!=0):
        print('B')
    if (x[1]==y[1] or x[3]==y[3] or x[5]==y[5]):
        print('C')
    else:
        print('None')   