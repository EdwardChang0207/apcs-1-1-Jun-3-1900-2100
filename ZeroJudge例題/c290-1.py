#input
n = input()
odd = [] #奇數
even = [] #偶數

#process
for i in range(len(n)):
    if i % 2 == 0: #奇數
        odd.append(int(n[i]))
    else: #偶數
        even.append(int(n[i]))

odd = sum(odd) #sum()取總和
even = sum(even)

ans = abs(odd - even) #absolute 絕對值

#output
print(ans)