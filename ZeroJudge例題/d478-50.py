#input
#n,m輸入後轉為int
# n, m = [int(i) for i in input().split()] #比較慢
n, m = map(int, input().split()) #比較快

#process
for _ in range(n):#共有n組
    #對每一組進行比較
    a = list(map(int, input().split())) #小潘
    b = list(map(int, input().split())) #小花

    result = 0 #統計結果
    for i in a: #用小潘的每一個數字去小花的對照
        if i in b:
            result += 1
    #output
    print(result) #輸出結果