import random


# Deck class - stores and actualizes an actual deck, pick random card from the deck
	def __init__(self, list_of_cards):
		self.list_of_cards = list_of_cards

	def pick_card(self):
		random_card = random.choice(self.list_of_cards)
		card_index = self.list_of_cards.index(random_card)		
		self.list_of_cards.pop(card_index)
		return random_card



# NPC class - stores, shows and counts a NPC's hand	
class NPC:
	def __init__(self, account, card_1, card_2):
		self.account = account
		self.card_1 = card_1
		self.card_2 = card_2
		self.hand = [self.card_1, self.card_2]
		self.value = 0

	def show_balance(self):
		print("NPC's balance - " + str(self.account))

	def take_new_card(self,additional_card):
		self.hand.append(additional_card)
		if additional_card == 'A':
			self.value += 11
		elif additional_card == 'K' or additional_card == 'Q' or additional_card == 'J':
			self.value += 10
		else:
			self.value += int(additional_card)

	def show_hand_before(self):
		print("NPC's hand: "+ "[" + str(self.card_1) + ", --- ]")

	def show_hand(self):
		print("NPC's hand: " + str(self.hand))

	def count_score(self):
		for card in self.hand:
			if card == 'A':
				self.value += 11
			elif card == 'K' or card == 'Q' or card == 'J':
				self.value += 10
			else:
				self.value += int(card)

	def score(self):
		return self.value

	def gain_lost(self, value, symbol):
		if (symbol == 'G' or symbol == 'g'):
			self.account += value
		elif (symbol == "L" or symbol == 'l'):
			self.account -= value
		else:
			print("Incorrect symbol!!!")


# Player class - inherits the functionality from NPC class - stores, shows and counts a player's hand
class Player(NPC):
	
	def __init__(self, account, card_1, card_2):
		NPC.__init__(self, account, card_1, card_2)
		

	
	def show_balance(self):
		print("Player's balance: " + str(self.account))


	def show_hand(self):
		print("Player's hand: " + str(self.hand))

		
#Below a code to run the game
		
check = True

while(check == True):

	cards = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,
		9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q'
		,'K','K','K','K','A','A','A','A']

	my_deck = Deck(cards)

	card_1 = my_deck.pick_card()
	card_2 = my_deck.pick_card()
	card_3 = my_deck.pick_card()
	card_4 = my_deck.pick_card()

	player_account = int(input("Enter your account balance: "))

	computer = NPC(player_account * 100, card_1, card_2)
	player = Player(player_account, card_3, card_4)


	while(player.account != 0 and player.account > 0):
		print(player.account)
		bet = int(input("How much would you like to bet?: "))
		while (bet > player.account):
			print("You can't bet more than you have, enter correct value: ")
			bet = int(input("Your bet: "))

		computer.show_hand_before()
		player.show_hand()

		computer.count_score()
		player.count_score()


		if player.score() == 21:
			print("Player has a BLACKJACK!	Player won")
			player.gain_lost(bet*3, 'g')
			computer.gain_lost(bet*1.5, 'l')

		
		while(player.score() < 21):
			choice = input("Would you like to hit (H) or stay (S)?:")
			if (choice == 'h' or choice == 'H'):
				player.take_new_card(my_deck.pick_card())
				player.show_hand()
				if player.score() == 21:
					print("Player has 21!	Player won")
					player.gain_lost(bet*2, 'g')
					computer.gain_lost(bet*1, 'l')
					break
				continue
			elif (choice == 's' or choice == 'S'):
				player.show_hand()
				computer.show_hand()
				while (computer.score() < 21):
					if (computer.score() <= 21 and computer.score() > player.score()):
						print("Dealer won")
						player.gain_lost(bet, 'l')
						computer.gain_lost(bet*2, 'g')
						break	
					computer.take_new_card(my_deck.pick_card())
					computer.show_hand()

				if (computer.score() < 21 and computer.score() > player.score()):
					break
				
				if (computer.score() > 21):
					print("NPC busted. Player won the bet")
					player.gain_lost(bet*2, 'g')
					computer.gain_lost(bet*1, 'l')
					break
		

		if (player.score() > 21):
			print("Player busted and lost his bet.")
			player.gain_lost(bet, 'l')
			computer.gain_lost(bet*2, 'g')

		my_deck = Deck(cards)

		card_1 = my_deck.pick_card()
		card_2 = my_deck.pick_card()
		card_3 = my_deck.pick_card()
		card_4 = my_deck.pick_card()

		npc_balance = computer.account
		player_balance = player.account

		computer = NPC(npc_balance, card_1, card_2)
		player = Player(player_balance, card_3, card_4)


	player_check = input("Would you like to keep playing?: Y(Yes), N(No)")

	if player_check == 'Y' or player_check == y:
		check = True
	elif player_check == 'N' or player_check == n:
		check = False
	else:
		print("Incorrect input")

print("Have a nice day")






					













