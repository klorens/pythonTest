from mpmath import mp

while True:
	try:
		n=int(raw_input("Select precision: "))
		if n >100:
			raise Exception("smaller than 100")
	except Exception as error:
		print error
		print "Try again!"
		continue
	else:
		break
def piPrec(n):
	mp.dps=n+1
	print mp.pi
	print mp.e

piPrec(n)
