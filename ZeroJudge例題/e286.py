game = 0 #贏的場次 if 主隊贏一場 then game += 1, else 客隊贏一場 then game -= 1
for j in range(2):
    #第一場
    x = list(map(int, input().split())) #主隊的分數
    y = list(map(int, input().split())) #客隊的分數
    r = 0 #最後結果 if r>0:主隊贏 else:客隊贏了
    for i in range(4): #0 1 2 3
        if x[i] > y[i]:
            r += 1 #-> r = r + 1 -> 後來的r = 原本的r + 1
        else:
            r -= 1
    if r > 0: #主隊贏了這一場
        game += 1
    else: #客隊贏了這一場
        game -= 1
    print('%d:%d'%(sum(x), sum(y))) #sum() -> 取總和
    # %d -> format 格式化
    # %d -> int, %f -> float, %s -> str
if game > 0:
    print('Win')
elif game == 0:
    print('Tie')
else:
    print('Lose')