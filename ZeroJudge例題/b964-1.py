#step1.input
#(1)人數
n = int(input()) #-> str: '10' -> 10
#(2)成績
s = input().split() #-> str: '0 11 22 33 55 66 77 99 88 44' -> ['0', '11', '22', 33 55 66 77 99 88 44']

#轉int:
#(1) for loop: slowest
# for i in range(len(s)):
#     s[i] = int(s[i])

#(2) for loop總和表達式: faster
# s = [int(i) for i in s]

#(3) map: fastest
s = list(map(int, s))

#step2. 排序
s.sort()
#(1) for loop:
# for i in s:
#     print(i, end=' ') #\n -> 換行
#(2) for loop 總和表達式:
# [print(i, end=' ') for i in s]
#(3) *
print(*s)

#step3.worst case
if s[-1] < 60:
    print(s[-1])
    print('worst case')

#step4. best case
elif s[0] >= 60:
    print('best case')
    print(s[0])

#step5. normal case
else:
    for i in range(len(s)):
        if s[i] >= 60:
            print(s[i-1]) #最高不及格
            print(s[i]) #最低及格

#DATE TYPE:
# number -> (1) int (2) float
# text -> string -> str
# booling -> bool -> (1) True (2) False
# list -> [n1, n2, n3]