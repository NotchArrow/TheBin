import random
import os

startingMoney = 1000
money = startingMoney
carGone = False
houseGone = False
lifeGone = False

# displaying cards neatly
def showcards(cards):
	for card in cards:
		print(card, end='')
		if len(cards) > cards.index(card) + 1:
			print(' | ', end='')
		else:
			print()

# score calculation
def getscore(cards):
	score = 0
	for card in cards:
		if 'King' in card:
			score += 10
		elif 'Queen' in card:
			score += 10
		elif 'Jack' in card:
			score += 10
		elif '10' in card:
			score += 10
		elif '9' in card:
			score += 9
		elif '8' in card:
			score += 8
		elif '7' in card:
			score += 7
		elif '6' in card:
			score += 6
		elif '5' in card:
			score += 5
		elif '4' in card:
			score += 4
		elif '3' in card:
			score += 3
		elif '2' in card:
			score += 2
		elif 'Ace' in card:
			score += 11
	return score

# checking for aces to save from bust
def checkaces(cards):
	aceCount = 0
	for card in cards:
		if 'Ace' in card:
			aceCount += 1
	return aceCount

# first bet
os.system('cls')
print('==============================')
print(f'You have ${money}')
bet = input('Place your bet (Type nothing to leave): ')
if bet.isnumeric():
	bet = int(bet)
	bet = abs(bet)
	if bet > money:
		bet = money
	money -= bet

os.system('cls')

# check to keep playing
while isinstance(bet, int):
	cardList = [
	'Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts',
	'8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts',
	
	'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', 
	'7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 
	'King of Diamonds',
	
	'Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs',
	'8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs',
	
	'Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades',
	'8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades'
	]

	# initial card drawing
	cardPicked = cardList[random.randint(0, len(cardList) - 1)]
	yourCards = [cardPicked]
	cardList.remove(cardPicked)
	cardPicked = cardList[random.randint(0, len(cardList) - 1)]
	dealerCards = [cardPicked]
	cardList.remove(cardPicked)

	cardPicked = cardList[random.randint(0, len(cardList) - 1)]
	yourCards.append(cardPicked)
	cardList.remove(cardPicked)
	cardPicked = cardList[random.randint(0, len(cardList) - 1)]
	dealerCards.append(cardPicked)
	cardList.remove(cardPicked)

	# info
	print('==============================')
	print(f'Your bet is ${bet}')
	print('You have ', end='')
	showcards(yourCards)
	yourScore = getscore(yourCards)
	print(f'That adds up to {yourScore}')
	print('Dealer is showing ' + dealerCards[0])

	# hit/stay
	choice = input("Hit or Stay?: ").lower()
	while choice == 'hit' or choice == 'h':
		os.system('cls')
		cardPicked = cardList[random.randint(0, len(cardList) - 1)]
		yourCards.append(cardPicked)
		cardList.remove(cardPicked)
		print('==============================')
		print(f'Your bet is ${bet}')
		print('You have ', end='')
		showcards(yourCards)
		yourScore = getscore(yourCards)
		if yourScore > 21:
			yourAces = checkaces(yourCards)
			if yourAces > 0:
				yourScore -= 10
		print(f'That adds up to {yourScore}')
		print('Dealer is showing ' + dealerCards[0])
		if yourScore > 21:
			break
		choice = input("Hit or Stay?: ").lower()

	# dealer hit/stay
	dealerScore = getscore(dealerCards)
	while dealerScore < 15 and dealerScore < yourScore and yourScore < 22:
		cardPicked = cardList[random.randint(0, len(cardList) - 1)]
		dealerCards.append(cardPicked)
		cardList.remove(cardPicked)
		dealerScore = getscore(dealerCards)
		if dealerScore > 21:
			dealerAces = checkaces(dealerCards)
			if dealerAces > 0:
				dealerScore -= 10

	# results
	os.system('cls')
	print('==============================')
	print(f'Your bet is ${bet}')
	print('You have ', end='')
	showcards(yourCards)
	yourScore = getscore(yourCards)
	if yourScore > 21:
		yourAces = checkaces(yourCards)
		if yourAces > 0:
			yourScore -= 10
	print(f'That adds up to {yourScore}')
	print()

	print('The dealer has ', end='')
	showcards(dealerCards)
	dealerScore = getscore(dealerCards)
	if dealerScore > 21:
		dealerAces = checkaces(dealerCards)
		if dealerAces > 0:
			dealerScore -= 10
	print(f'That adds up to {dealerScore}')
	print()

	# outcome
	if yourScore <= 21:
		if dealerScore <= 21:
			if dealerScore >= yourScore:
				print('Dealer wins')
				print(f'You lost ${bet}')
				print(f'You now have ${money}')
			else:
				money += bet * 2
				print('You win')
				print(f'You won ${bet}')
				print(f'You now have ${money}')
		else:
			money += bet * 2
			print('Dealer BUSTS!')
			print(f'You won ${bet}')
			print(f'You now have ${money}')
	else:
		print('You BUST!')
		print(f'You lost ${bet}')
		print(f'You now have ${money}')
	input('==============================')

	# anti bankrupt
	if money == 0:
		os.system('cls')
		print('==============================')
		if carGone == False:
			print('Automatically sold your car for $500')
			carGone = True
			money += 500
		elif houseGone == False:
			print('Automatically sold your house for $1000')
			houseGone = True
			money += 1000
		elif lifeGone == False:
			print('Automatically withdrew all of your life savings for $3000')
			lifeGone = True
			money += 3000
		else:
			print('The house always wins')
			print('You have officially lost everything')
			print('Remember that 99% of gamblers quit before they win big')
		input('==============================')

	# new bet
	if money > 0:
		os.system('cls')
		print('==============================')
		print(f'You have ${money}')
		bet = input('Place your bet (Type nothing to leave): ')
		if bet.isnumeric():
			bet = int(bet)
			bet = abs(bet)
			if bet > money:
				bet = money
			money -= bet
	else:
		bet = 'none'

# what happened overall
os.system('cls')
print('==============================')
print(f'You left with ${money}')
if money > startingMoney:
	print(f'You won ${money - startingMoney}!')
elif money < startingMoney:
	print(f'You lost ${startingMoney - money}')
	print('Remember that 99% of gamblers quit before they win big')
elif money == startingMoney:
	print("You didn't lose anything!")
print('==============================')
if carGone:
	print('If you forgot, your car is gone. You get to walk home!')
if houseGone:
	print("Wait! Your house is gone too! Guess you'll have to buy a cardboard box!")
if lifeGone:
	print("Although you can't afford one because your life savings are gone too")
	print()
	print()
	print(':(')