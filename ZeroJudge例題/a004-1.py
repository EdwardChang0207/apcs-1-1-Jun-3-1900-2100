import sys #library -> 函式庫 sys -> system
for x in sys.stdin: #x -> 每一次拿到的input:str, stdin -> standard input
    x = int(x) #後來的x = 原本的x轉整數
    if (x % 4 == 0 and x % 100 != 0) or (x % 400 == 0):
        print('閏年')
    else:
        print('平年')