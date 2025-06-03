#input
a, b, c = map(int, input().split())
a, b, c = map(bool, [a, b, c])

#process
ans = []
if (a and b) == c:
    ans.append('AND')
if (a or b) == c:
    ans.append('OR')
if ((a or b) and (not(a and b))) == c:
    ans.append('XOR')

#output
if ans:
    print(*ans, sep='\n')
else:
    print('IMPOSSIBLE')