codeOne = [4, 3, 10, 2, 8]
targetOne = 12

codeTwo = [1, 2, 3, 4]
targetTwo = 15

codeThree = [1,1,1,1,1,1,1]
targetThree = 7


def answer(l,t):
	firstIndex = lastIndex = counter = 0
	checkTarget = 0
	for element in l:

		for i in range(firstIndex, len(l)):
			checkTarget = checkTarget + l[i]
			if checkTarget == t:
				lastIndex = firstIndex + counter
				return ([firstIndex,lastIndex])
			elif checkTarget > t:
				break
			counter += 1
		firstIndex += 1
		checkTarget = 0
		counter = 0

	return [-1,-1]

print (answer(codeOne,targetOne))
print (answer(codeTwo,targetTwo))
print (answer(codeThree,targetThree))


# firstIndex = 0
# lastIndex = 0
# counter = 1
# element = 1
# checkTarget = 1
# t = 7
# i = 1
# length = 7