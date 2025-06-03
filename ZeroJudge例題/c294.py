# 讀取輸入，轉為整數並存於list
s = list(map(int, input().split())) #['3','4','5'] -> [3, 4, 5]
# 排序：小->大
s.sort()
# 輸出排序後的邊長
print(*s) # *:for all -> 3 4 5
#檢查是否能夠成三角形
if s[0]+s[1] <= s[2]: #不能構成三角形
    print('No')
else:
    # 判斷可以構成何種三角形
    if s[0]**2+s[1]**2 < s[2]**2:
        print('Obtuse')
    elif s[0]**2+s[1]**2 == s[2]**2:
        print('Right')
    else:
        print('Acute')
