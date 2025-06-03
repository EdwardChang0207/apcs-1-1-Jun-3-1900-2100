# 讀取地圖大小和初始參數
M, N, k, r, c = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(M)]
score = 0
facing = [0, 1]  # 初始朝向右
result = 0

# 定義向右轉90度的函數
def turn(facing):
    if facing == [0, 1]:       # 向右 -> 向下
        return [1, 0]
    elif facing == [1, 0]:     # 向下 -> 向左
        return [0, -1]
    elif facing == [0, -1]:    # 向左 -> 向上
        return [-1, 0]
    elif facing == [-1, 0]:    # 向上 -> 向右
        return [0, 1]

# 主迴圈：檢查當前位置的寶石數量
while game_map[r][c] != 0:
    score += game_map[r][c]
    result += 1
    game_map[r][c] -= 1  # 拿走一顆寶石

    # 如果 score 是 k 的倍數，則轉向
    if score % k == 0:
        facing = turn(facing)
    
    # 確保下一步不會碰到牆壁或邊界
    while (r + facing[0] >= M or r + facing[0] < 0 or 
           c + facing[1] >= N or c + facing[1] < 0 or 
           game_map[r + facing[0]][c + facing[1]] == -1):
        facing = turn(facing)

    # 更新機器人位置
    r += facing[0]
    c += facing[1]

# 輸出機器人總共蒐集的寶石數量
print(result)
