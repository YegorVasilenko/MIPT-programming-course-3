def f(n):
	if n <= 1:
		return n
	return f(n-1) + f(n-2)


n = int(input()) - 1
print(f(n))
