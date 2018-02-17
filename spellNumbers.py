from collections import OrderedDict

n=int(raw_input("input number here: "))
def spellNumber(n):
	ranges=OrderedDict([('quadrillion',10e14),('trillion',10e11),('billion',10e8),('million',10e5),('thousand',10e2),('hundred',100)])
	tens=OrderedDict([('ten',10),('twenty',20),('thirty',30),('fourty',40),('fifty',50),('sixty',60),('seventy',70),('eighty',80),('ninety',90)])
	teens=OrderedDict([('ten',10),('eleven',11),('twelve',12),('thirteen',13),('fourteen',14),('fifteen',15),('sixteen',16),('seventeen',17),('eighteen',18),('nineteen',19)])
	digits=OrderedDict([('one',1),('two',2),('three',3),('four',4),('five',5),('six',6),('seven',7),('eight',8),('nine',9)])
	
	def lowNumbers(n):
		numStr=""
		while n > 0:
	               if n >= 20 and n < 100:
	       	                howMany=int(n/10)
	               	        n=n%10
	                       	for rg,val in tens.items():
	                                if howMany*10 == val:
	                                       	numStr+=rg
	                                        break
	               elif n >=10:
	                        for rg,val in teens.items():
	                                if n == val:
	                                        numStr+=rg
	                                        n=n-val
	                                        break
	               else:
	       	                for rg,val in digits.items():
	              	                if n == val:
						if numStr=="":
		                       	                numStr+=rg
						else:
							numStr+='-'+rg
		                                n=n-val
	                                        break
		return numStr
	
	vals=[]
	rgs=[]
	while n >= 100:
		for rg,val in ranges.items():
			if n >= val:
				howMany=int(n/val)
				n=n-howMany*val
				if howMany > next(reversed(ranges.values())):
					hundreds=howMany/next(reversed(ranges.values()))
					vals.append(hundreds)
					rgs.append(next(reversed(ranges))+' ')
					howMany=howMany-hundreds*next(reversed(ranges.values()))
				vals.append(howMany)
				rgs.append(rg+' ')
				break
	else:
		lows=lowNumbers(n)
	
	bigs=[]
	for n in vals:
		bigs.append(lowNumbers(n))
	result = [str(val)+' '+str(rg) for val, rg in zip(bigs,rgs)]
	result.append(lows)
	
	result=''.join(result)
	print result

spellNumber(n)
