def answer(start, length):
	lis = list(range(start, start+(length**2)))
	checksum = 0
	counter = 0
	for i in range(0,length):
		for j in range(counter,(counter+length)-i):
			checksum = checksum ^ lis[i+j]
			counter = j + i
	return checksum
print (answer(17,4))


# 17 18 19 20 / 21 22 23 24 / 25 26 27 28 / 29 30 31 32
# 17 18 19 20 21 22 23 26 26 29

# length = 10
# def pri(length):
# 	counter = 0
# 	for i in range (0,length):
# 		for j in range(counter,(counter+length)-i):
# 			print (i+j,end='\t')
# 			counter = j
# 		print(end='\n')
# pri(length)


# 0,0		0,1		0,2
# 0		1		2

# 1,2		1,3
# 3		4		
	
# 2,3
# 5

# i = 1
# j = 2
# counter = 2

# 0	1	2
# 3	4


# 0,0		0,1		0,2		0,3
# 0		1		2		3

# 1,3		1,4		1,5		#1,6
# 4		5		6		#7	
	
# 2,6		2,7		#2,8		2,9
# 8		9		#10		11

# 3,9		#3,10	3,11	3,12	
# 12		#13		14		15

# length = 4
# def pri(length):
# 	counter = 0
# 	for i in range (0,length):
# 		for j in range(counter,(length + counter) - i):
# 			print (i+j,end='\t')
# 			# print (counter)
# 			counter = j + i
# 		print(end='\n')
# pri(length)




















