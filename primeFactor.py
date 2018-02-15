n=600851475143546546
f=2
def findPrimeFactors(n):
	result=[]
	while f*f <= n:
		for i in xrange(f,n+1):
			if n%i==0:
				n=n/i
				print i
				break

findPrimeFactors(n)
