n = int(input())
s = [list(map(int, input().split())) for _ in range(n)] 
d = [abs(s[i][0]-s[i+1][0])+abs(s[i][1]-s[i+1][1]) for i in range(len(s)-1)]

# for i in range(len(s)-1):
#     d.append(abs(s[i][0]-s[i+1][0])+abs(s[i][1]-s[i+1][1]))

print(max(d),min(d))