#input
a, b, c = list(map(int, input().split()))
n = False
#process
#True
if c:
    if a and b:
        print('AND')
        n = True
    if a or b:
        print('OR')
        n = True
    #assume a = T, b = F assume a = F, b = T
    if (a and not(b)) or (not(a) and b):
        print('XOR')
        n = True
else:
    if not(a and b):
        n = True
        print('AND')
    if not(a or b):
        n = True
        print('OR')
    if not((a and not(b)) or (not(a) and b)):
        n = True
        print("XOR")
if not n:
    print("IMPOSSIBLE")