hallwayOne = '--->-><-><-->-'
hallwayTwo = '>----<'
hallwayThree = '<<>><'
hallwayFour = '<<<<<--------->>>>>'

def answers(s):
	ctr = 0
	salute = 0
	for person in s:
		if person == '>':
			front = s[ctr:]
			for oncoming in front:
				if oncoming == '<':
					salute += 2
		ctr += 1			

	return salute				






## HIS Version
# def answers(s):
# 	salute = 0
# 	counter = 0
# 	for person in s:
# 		if person == '>':
# 			counter += 1
# 		elif person == '<':
# 			salute += counter

# 	return salute * 2

print (answers(hallwayFour))