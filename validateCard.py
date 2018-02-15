cardNumber='5571246077010947'
def validateCard(cardNumber):
	tmp=[int(s) for s in cardNumber[:len(cardNumber)-1]]
	vn=int(cardNumber[-1])
	if len(cardNumber) == 16:
		for i in range(len(tmp)):
			tmp[i] =int(tmp[i]*2)
			if tmp[i] >=10:
				tmp[i] = str(tmp[i])
				tmp[i]=int(tmp[i][0])+int(tmp[i][1])
		tmp=reduce(lambda x,y: x+y,tmp)
	else:
		return false
	return (tmp+vn)%10==0

print validateCard(cardNumber)
