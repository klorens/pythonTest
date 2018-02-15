import random

class Player():
	def __init__(self, name='Player1', bankroll=1000, mode='human',isActive=True):
		self.name = name
		self.bankroll = bankroll
		self.mode = mode
		self.cards = []
		self.points=0
		self.isActive=isActive
		self.play = True
		self.bet=0
	
	def userStartMessage(self):
		if self.mode=='human':
			show_cards=""
			for i in self.cards:
	                        show_cards+=str(str(i[0])+str(i[1])+",")
			print("You have {}$".format(self.bankroll))
			print("Player "+self.name+" your cards "+show_cards+" score: "+str(self.points))
		else:
			print("Croupier has card: "+str(self.cards[0]))

	def betSelect(self):
		while True:
			try:
				bet=int(raw_input("Your bet is: "))
				if bet > self.bankroll:
					raise Exception("Bet bigger than bankroll")
			except Exception as e:
				print repr(e)
				continue
			except:
				print "Try again!"
				continue
			else:
				self.bet=bet
				break
		

	def update_bankroll(self, amount):
		self.bankroll += amount
	
	def set_cards(self, deck):
		self.cards=[]
		for i in range(2):
			self.cards.append(deck.pop())
		return self.cards
	
	def show_cards(self):
		for i in self.cards:
			print (str(i[0])+str(i[1])),

	def hit_card(self,deck):
		self.cards.append(deck.pop())
		return self.cards

	def stand(self):
		self.isActive=False
		return self.cards

	def double_down(self,deck):
		self.isActive=False
		self.cards.append(deck.pop())
                return self.cards

	def split_cards(self, deck):
		cards2=self.cards.pop()
		self.cards.append(deck.pop())
		cards2.append(deck.pop())
		return self.cards, cards2

	def update_points(self, value):
		self.points=value
		return self.points

	def isBlackJack(self):
		if self.points == 21:
			self.isActive=False
			return True
		else:
			return False

	def isBoosted(self):
		if self.points > 21:
			self.isActive=False
			return True
		else:
			return False

	def finishRound(self,result):
		if result==0:
			print "Push"
		elif result > 0:
			print "You won!"
			self.bankroll+=self.bet
		else:
			print "You lost..."
			self.bankroll-=self.bet
		if self.bankroll > 0:
			finishGame=raw_input("Do you want to continue? y/n: ")
			if finishGame == 'n':
				self.play = False
			self.isActive = True
		else:
			print "You do not have money to play. Try again."
			self.play = False

class Deck():
	faces={2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':10,'Q':10,'K':10,'A':[1,11]}
	suits={'C':'Club','S':'Spade','D':'Diamond','H':'Heart'}
	
	def create_deck(self):
		deck=[]
		for s in Deck.suits.keys():
			for f in Deck.faces.keys():
				deck.append([f,s])
		random.shuffle(deck)
		return deck

	def get_card_values(self, cards):
		tmp=[]
		for i in cards:
			if i[0] == 'A':
				tmp.append(i)
				cards.remove(i)
		if len(tmp):
			for i in tmp:
				cards.append(i)
		score=0
		for i in cards:
			if i[0] != 'A':
				score+=self.faces[i[0]]
			else:
				if score < 11:
					score+=self.faces[i[0]][1]
				else:
					score+=self.faces[i[0]][0]
		return score
	
	def gameResults(self,human,croupier):
		result=(human-croupier)
		return result
		

d = Deck()
myPlayer=Player('Kris')
croupier=Player(name='Croupier', mode='computer')
Game=True

while myPlayer.play==True:
	deck=d.create_deck()
#	myPlayer.cards=[[8,'S'],[8,'C']]
	myPlayer.set_cards(deck)
	croupier.set_cards(deck)
	myPlayer.update_points(d.get_card_values(myPlayer.cards))
	options={'Split':False,'Hit card':True,'Double':True,'Stand':True}
	print "\n<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>\n"
	print "Let's start the game!"
	myPlayer.userStartMessage()
	croupier.userStartMessage()
	myPlayer.betSelect()
	while not myPlayer.isBoosted():
		if len(myPlayer.cards) == 2 and myPlayer.cards[0][0] == myPlayer.cards[1][0]:
			options['Split'] = True
		if len(myPlayer.cards) > 2:
			options['Double'] = False
		
		print "Select what you want to do next: "
		choice=[]
		index = 1
		for key in options.keys():	
			if options[key] == True:
				print(str(index)+": "+str(key))
				choice.append(key)
				index+=1
		if myPlayer.isBlackJack():
                       	print "Black Jack!!!!"
		while myPlayer.isActive:
			try:
				selection=int(raw_input("Type your choice: "))
			except:
				print "Try again!"
				continue
			else:
				if choice[selection-1] == 'Split':
					myPlayer.split_cards(deck)
					options['Split'] = False
				elif choice[selection-1] == 'Double':
					myPlayer.double_down(deck)
				elif choice[selection-1] == 'Hit card':
					myPlayer.hit_card(deck)
				elif choice[selection-1] == 'Stand':
					myPlayer.stand()
				else:
					print "unexpected error"
				break
		myPlayer.update_points(d.get_card_values(myPlayer.cards))
		print "Your hand is ", myPlayer.cards, "and you have " ,myPlayer.points,"\n"
		if not myPlayer.isActive:
			croupier.update_points(d.get_card_values(croupier.cards))
			print croupier.name,"cards are ",croupier.cards,"score:", croupier.points
			while not croupier.isBoosted():
				if croupier.points < 17:
					print "Croupier takes additional card"
					croupier.hit_card(deck)
					croupier.update_points(d.get_card_values(croupier.cards))
					print croupier.name,"cards are ",croupier.cards,"score:", croupier.points
				else:
					myPlayer.finishRound(d.gameResults(myPlayer.points,croupier.points))
					break
			else:
				print "croupier boosted!!!"
				myPlayer.finishRound(1)
				break
			break
	else:
		print "Player boosteed"
		myPlayer.finishRound(-1)
		continue
