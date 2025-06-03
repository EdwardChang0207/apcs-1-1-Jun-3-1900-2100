x = input() #str eg.'123456'
A = list(x[0::2])
B = list(x[1::2])
A = sum(list(map(int, A)))
B = sum(list(map(int, B)))
print(abs(A-B))