#input
N, M = list(map(int, input().split()))
numbers = [] #所有的數 n(row)*m(col)
s_list = [] #每一群的最大值
a = [] #存可以整除s的數

#process
for i in range(N):
    row = list(map(int,input().split())) #每一行
    s_list.append(max(row)) #紀錄每一群的最大值
    numbers.append(row) #紀錄所有的數

s = sum(s_list) #算出s的值

for i in s_list:
    if s % i == 0: #檢查看是否有選到的數可以整除s
        a.append(i)
#output
print(s) #輸出s的值
if a: #檢查是否有數可以整除s，如果有：輸出每一個，否則輸出-1
    print(*a)
else:
    print(-1)


