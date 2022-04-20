#!/usr/bin/env python

def plus(a, b):
	return a + b

def minus(a, b):
	return a - b

def times(a, b):
	return a * b

def divide(a, b):
	return a / b

def math_table(a, operator, b):
	table = {
		'+': plus,
		'-': minus,
		'*': times,
		'/': divide
	}

	return table[operator](a, b)

