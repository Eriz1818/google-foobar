# def answer(n):
# 	return len([(x,y) for x in range(0,n) for y in range (0,n) if x >=1 and y >= 1 and x != y and x+y==n])//2

# print (answer(200))

def answer(n):
	lookup = {}
	posib = 0

	if n <3:
		return "Incorrect Value"
	elif n>=3 and n<=200:
		for number in range (3,n+1):

			posib = [(x,y) for x in range(0,number) for y in range (0,number) if x >=1 and y >= 1 and x != y and x+y==number and x > y]
			lookup[number] = len(posib)
			

	else:
		return "Commander Lambda is not made of money :O"

print (answer(4))	