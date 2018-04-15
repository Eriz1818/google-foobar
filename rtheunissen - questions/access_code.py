lis = ['abc', 'cba', 'bca', 'nitin', 'baby', 'ybab', 'awesome', 'emosewa', 'nitin', 'meow', 'woem', 'test']

def answer(x):
	repeat = 0
	for item in x:
		if item[::-1] in x:
			repeat += 1
	return len(x) - repeat//2

print (answer(lis))
