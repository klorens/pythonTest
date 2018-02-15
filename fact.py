def fact(n):
	fact=1
	if n in (0,1):
		return 1
	else:
		for i in range(1,n+1):
			fact=fact*i
	return fact

print fact(1000)
