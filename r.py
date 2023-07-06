# 讀取檔案
# 每讀一千筆印一次

data = [] #空清單
count = 0 #指定 count 為計數並從零開始
with open('reviews.txt', 'r')as f: # 開啟檔案
	for answer in f: # 做 for 迴圈從 f 取出每一行
		data.append(answer.strip()) # 把每一行存進 data 清單中
		count += 1 # 計算個數
		# if count % 1000 == 0: # 只印每 1000 筆 
		# 	print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

# sum_len = 0
# for d in data:
# 	sum_len += len(d)

# print('留言的平均長度是', sum_len/len(data))

# new = [] # 空清單
# for d in data: # 從 data 中取出每一個字串為 d
# 	if len(d) < 100: # 從 d 中篩出字數少於 100 的字串
# 		new.append(d) # 再把字串放回 new 清單中
# print('一共有', len(new), '筆留言長度小於 100')	
# print(new[0])
# print(new[1])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d)
# print('一共有', len(good), '筆留言含有good')
# print(good[0])

# good = [d for d in data if 'good' in d]
# output = 運算 for 變數 in 清單 if 篩選條件
# print('一共有', len(good), '筆留言含有good')
# print(good)

# bad = ['bad' in d for d in data]
# print(bad)

# bad = []
# for d in data:
# 	bad.append('bad' in d)

# 文字計數
wc = {} #word_count

for d in data:
	words = d.split()
	for word in words:
		if word in wc: # 如果 word 有在 wc 中出現過
			wc[word] += 1 # 去 wc 中找配對過的字並加一
		else:
			wc[word] = 1 # 新增 key 

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word]) # 右邊的意思是在 wc 中找尋這個 key
print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字？')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為：', wc[word])
	else:
		print('這個字沒有出現過喔')
print('感謝使用本查詢功能')
















