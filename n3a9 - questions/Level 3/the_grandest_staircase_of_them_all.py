def answer(n):
	memo = [[0 for i in range(n + 1)] for j in range(n + 1)]
	memo[0][0] = 1
	for row in range(1, n + 1):
	    for col in range(0, n + 1):
	        memo[row][col] = memo[row - 1][col]
	        if col >= row:
	            memo[row][col] += memo[row - 1][col - row]
	        # print ('for row: {} col: {} matrix: {}'.format(row,col,memo))
	return memo

num = 13
memo = answer(num)
print(memo[num][num] - 1)
