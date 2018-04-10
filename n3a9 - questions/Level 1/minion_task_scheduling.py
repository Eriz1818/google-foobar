def answer(data,n):
	dic = {}
	for num in data:
		if num in dic:
			dic[num] = dic[num] + 1
		else:
			dic[num] = 1
	# print (dict)
	for key in dic:
		if dic[key] > n:
			for _ in range(0,dic[key]):
				data.remove(key)
	return data

lis = [1, 2, 3]
print (answer(lis, 6))