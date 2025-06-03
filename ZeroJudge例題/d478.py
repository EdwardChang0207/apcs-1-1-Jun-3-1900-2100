#input
#n,m輸入後轉為int
n, m = map(int, input().split()) #比較快

#process
for _ in range(n):#共有n組
    #對每一組進行比較
    a = set(map(int, input().split())) #小潘(集合)
    b = set(map(int, input().split())) #小花(集合)

    #output
    print(len(a&b)) #輸出結果