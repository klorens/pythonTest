n=0
selection=""
def isPrime(n):
	if n in [1,2,3]:
		return True
	else:
		for i in range(2,n):
			if n%i==0:
				return False
				break
		return True

while True:
	n+=1
	if isPrime(n):
		print n
#		selection=raw_input("Do you want to get next prime number?: (y/n) ")

