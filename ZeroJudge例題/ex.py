questions = [ #問題清單
	'3+5=?',
	'4-2=?'
]
ans = [ #答案清單
	'8',
	'2'
]
reward = 0 #累計獎金
combo = 0 #連續答對
for i in range(len(questions)): #i即為題號
    print(questions[i])
    if input() == ans[i]:#如果答對
        reward += (i+1)*300*(1+0.1*combo)
        combo += 1
    else: #答錯
        combo = 0
print('恭喜你獲得了%d元'%(reward))#輸出結果