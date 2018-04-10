lisOne = [1, 2, 3, 4, 5, 6]
lisTwo = [1, 1, 1]


def answer(l):
	return len([(x,y,z) for x in l for y in l for z in l if (x < y and y%x == 0) and (y < z and z%y == 0)]) if len([(x,y,z) for x in l for y in l for z in l if (x < y and y%x == 0) and (y < z and z%y == 0)]) > 0 else 0

print (answer(lisOne))
print (answer(lisTwo))
