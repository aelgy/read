# 讀取檔案
# 每讀一千筆印一次

data = []
count = 0 
with open('reviews.txt', 'r')as f:
	for answer in f:
		data.append(answer.strip())
		count += 1
		if count % 1000 == 0:
			print(len(data))