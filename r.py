# 讀取檔案
# 每讀一千筆印一次

data = [] #空清單
count = 0 #指定 count 為計數並從零開始
with open('reviews.txt', 'r')as f: # 開啟檔案
	for answer in f: # 做 for 迴圈從 f 取出每一行
		data.append(answer.strip()) # 把每一行存進 data 清單中
		count += 1 # 計算個數
		if count % 1000 == 0: # 只印每 1000 筆 
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

# sum_len = 0
# for d in data:
# 	sum_len += len(d)

# print('留言的平均長度是', sum_len/len(data))

new = [] # 空清單
for d in data: # 從 data 中取出每一個字串為 d
	if len(d) < 100: # 從 d 中篩出字數少於 100 的字串
		new.append(d) # 再把字串放回 new 清單中
print('一共有', len(new), '筆留言長度小於 100')	
print(new[0])
print(new[1])










