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
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)

print('留言的平均長度是', sum_len/len(data))









