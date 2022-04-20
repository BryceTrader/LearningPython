#!/usr/bin/env python
import sys

def plus(a, b):
	return a + b

def minus(a, b):
	return a - b

def times(a, b):
	return a * b
	
def divide(a, b):
	return a / b

def math(a, operator, b):
	switch = {
		'+': plus,
		'-': minus,
		'x': times,
		'/': divide
	}

	return switch[operator](a, b)

def order_of_operations(ui):
	for i, char in enumerate(ui):
		if char == '/' or char == 'x':
			a = int(ui[i-1])
			opt = ui[i]
			b = int(ui[i+1])
			
			lower = ui[:i-1] + [None, None]
			middle = [math(a, opt, b)]
			upper = ui[i+2:]
			ui = lower + middle + upper
			i -= 2
	# removing None indexes
	ui = [x for x in ui if x]
	
	for i, char in enumerate(ui):
		if char == '+' or char == '-':
			a = int(ui[i-1])
			opt = ui[i]
			b = int(ui[i+1])
			
			lower = ui[:i-1] + [None, None]
			middle = [math(a, opt, b)]
			upper = ui[i+2:]
			ui = lower + middle + upper
			i -= 2
	# removing None indexes
	ui = [x for x in ui if x]
	return ui[0]

user_input = sys.argv[1:]
result = order_of_operations(user_input)
print(result)