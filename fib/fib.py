from time import perf_counter

# 
# Fast doubling Fibonacci algorithm (Python)
# 
# Copyright (c) 2015 Project Nayuki. Public domain.
# https://www.nayuki.io/page/fast-fibonacci-algorithms
# 


# (Public) Returns F(n).
def fibonacci(n):
	if n < 0:
		raise ValueError("Negative arguments not implemented")
	return _fib(n)[0]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n):
	if n == 0:
		return (0, 1)
	else:
		a, b = _fib(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return (c, d)
		else:
			return (d, c + d)


def fast_fib(x):
	a = 0
	b = 1

	for i in range(x):
		a, b = b, a
		b += a

	return a


def slow_fib(x):
	if x <= 0:
		return 0
	if x == 1:
		return 1
	return slow_fib(x - 1) + slow_fib(x - 2)
	

def main():
	# start = perf_counter()
	# print(fast_fib(50))
	# stop = perf_counter()

	# print(stop - start)

	x = 500000
	fstart = perf_counter()
	fast_fib(x)
	fend = perf_counter()
	# sstart = perf_counter()
	# s = slow_fib(x)
	# send = perf_counter()

	fast = perf_counter()
	fibonacci(x)
	faste = perf_counter()

	print(f'Fast: {fend - fstart} Really fast: {faste - fast}')

if __name__ == '__main__':
	main()