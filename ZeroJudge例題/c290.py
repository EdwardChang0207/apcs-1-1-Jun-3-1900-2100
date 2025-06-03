#step1. input
n = input() #'1987391'
odd = []
even = []
for i in range(len(n)): #0~n-1
    if i % 2 == 0: #奇數項
        odd.append(int(n[i]))
    else: #偶數項
        even.append(int(n[i]))

ans = abs(sum(odd)-sum(even))
print(ans)
