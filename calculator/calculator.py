#!/usr/bin/env python

def plus(a, b):
	return a + b

def minus(a, b):
	return a - b

def times(a, b):
	return a * b
	
def divide(a, b):
	return a / b

def math(a, b, operator):
	switch = {
		'+': plus,
		'-': minus,
		'*': times,
		'/': divide
	}

	return switch[operator](a, b)

