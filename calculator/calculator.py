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
		'*': times,
		'/': divide
	}

	return switch[operator](a, b)

def order_of_operations(ui, opts):
	for i, char in enumerate(ui):
		if char == opts[0] or char == opts[1]:
			a = int(ui[i-1]) if isinstance(ui[i-1], str) else ui[i-1]
			opt = ui[i]
			b = int(ui[i+1]) if isinstance(ui[i+1], str) else ui[i+1]
			
			lower = ui[:i-1] + [None, None]
			middle = [math(a, opt, b)]
			upper = ui[i+2:]
			ui = lower + middle + upper
			i -= 2
	# removing None indexes
	return [x for x in ui if x]

def use_input(ui):
	opts = [['*', '/'], ['+', '-']]
	for opt in opts:
		ui = order_of_operations(ui, opt)

	return ui[0]

def filter_input(ui):
	for i, x in enumerate(ui):
		if x == __file__[2:]:
			ui[i] = '*'
	print(ui)
	return use_input(ui)

user_input = sys.argv[1:]
result = filter_input(user_input)
print(result)