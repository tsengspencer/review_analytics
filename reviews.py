data = []
count = 0 # 可以通過計數知道讀取進度
sum_length = 0 
with open("reviews.txt","r") as f:
		for line in f:
			data.append(line)
			count += 1 # count = count + 1 
			sum_length = sum_length + len(line)
			if count % 1000 == 0: #每一千筆的餘數為0(%取餘數)
				print(len(data)) #確保讀取進度
print("檔案讀取完畢", "總共有", len(data), "筆資料")
print("每筆留言的平均長度為", sum_length/len(data))
