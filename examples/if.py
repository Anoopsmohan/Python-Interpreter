a = 100
b = a
while b:
	b = b - 25
	a = a - 10
	if b:
		j = 10
		while j:
			print a
			a = a - 1
			j = j - 1
	else:
		print 1234
