from random import randint

def roll(dice):
	space_break = dice.split(' ')
	i = 0
	total = 0
	while i < len(space_break) - 1:
		a = validate(space_break[i])
		operation = space_break[i+1]
		b = validate(space_break[i+2])
		total += switch_math(a, operation, b)
		i += 2
		
	
	return total

def validate(str):
	result = list(map(int, str.split('d')))
	if len(result) > 1:
		result = generateRoll(result)
	else:
		result = result[0]
	return result

def generateRoll(arr):
	num_dice, max = arr
	total = 0
	for die in range(num_dice):
		total += randint(1, max)
	return total

def plus(a, b):
	return a + b

def minus(a, b):
	return a - b

def switch_math(a, operator, b):
	switch = {
		'+': plus,
		'-': minus
	}
	
	result = switch[operator](a, b)
	return result

def main():
	while True:
		dice = input('Input the dice to roll... ')
		if dice == 'exit':
			break
		result = roll(dice)
		print(result)

if __name__ == '__main__':
	main()