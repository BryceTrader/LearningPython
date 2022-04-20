#!/usr/bin/env python
import sys

def fizzbuzz(y):
	for x in range(1, y+1):
		if (x % 3 == 0) and (x % 5 == 0):
			print('Fizzbuzz')
		elif x % 3 == 0:
			print('Fizz')
		elif x % 5 == 0:
			print('Buzz')
		else:
			print(x)

upto = sys.argv[1]
if upto.isdecimal():
	upto = int(upto)
	fizzbuzz(upto)
else:
	print('Invalid input.')