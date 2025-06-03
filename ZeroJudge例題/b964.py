#input, list, condition
n = int(input()) #學生人數

s = list(map(int,input().split())) #scores
s.sort() #排序

print(*s) #輸出所有成績（小到大）

if s[0] >= 60: #best case:
    print('best case')
    print(s[0]) #全部及格，所以全班最低分就是最低及格分數
    
elif s[-1] < 60: #worst case
    print(s[-1]) #全部不及格，所以全班最高分就是最高不及格分數
    print('worst case')

else: #normal case -> 尋找最低及格，前一個就是最高不及格
    for i in range(len(s)):
        if s[i] >= 60:
            print(s[i-1])
            print(s[i])