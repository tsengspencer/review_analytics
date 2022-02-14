data = []
count = 0 # 可以通過計數知道讀取進度
with open("reviews.txt","r") as f:
		for line in f:
			data.append(line)
			count += 1 # count = count + 1 
			if count % 1000 == 0: #每一千筆的餘數為0(%取餘數)
				print(len(data)) #確保讀取進度

