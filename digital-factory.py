import re
import random

#1

def sum_multi():
	sum = 0
	threes = 3
	while threes < 1000:
		sum += threes
		threes += 3

	fives = 5
	while fives < 1000:
		sum += fives
		fives += 5

	return sum

print sum_multi()

#2

def even_fib():
	sum = 0
	count = [1, 2]
	while count[-1] <= 4000000:
		count.append(count[-1] + count[-2])

	count.pop(-1)

	for num in count:
		if num % 2 == 0:
			sum += num
	return sum

print even_fib()

#3

def longest_substring(string):
	substrings = []
	substring = ""
	for char in string:
		if char in substring:
			substrings.append(len(substring))
			substring = ""
		else:
			substring += char

	longest_substring = substrings[0]

	for length in substrings:
		if length > longest_substring:
			longest_substring == length

	return longest_substring

print longest_substring("bbbbb")

SUITS = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
VALUES = ["Ace",1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
# a card consists of a string suite and a string value
class Card(object):

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __str__(self):
		return self.value+" of "+self.suit

# a deck consists of an array of cards
class Deck(object):

	def __init__(self, cards):
		self.cards = cards

	def __str__(self):
		return " ".join([str(card) for card in self.cards])

	def shuffle(self):
		shuffled_deck = []
		for card in self.cards:
			shuffled_deck.append(card)
		random.shuffle(shuffled_deck)
		self.cards = shuffled_deck		

def deck_creator(suits=SUITS,values=VALUES):
	deck_array =  []
	for suit in suits:
		for value in values:
			card = Card(value = str(value), suit = suit)
			deck_array.append(card)
	deck = Deck(deck_array)
	return deck


deck = deck_creator()
print deck
deck.shuffle()
print deck









