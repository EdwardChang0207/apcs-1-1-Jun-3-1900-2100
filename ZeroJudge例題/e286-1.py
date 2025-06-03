r = 0
for i in range(2):
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print('%d:%d'%(sum(a), sum(b))) #format
    if sum(a) > sum(b):
        r += 1
    else:
        r -= 1

if r > 0:
    print('Win')
elif r == 0:
    print('Tie')
else:
    print('Lose')