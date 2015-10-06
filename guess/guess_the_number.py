from random import randint
guess = randint(1,100)
while True:
	n = input()
	if n == guess:
		print "your guess is correct"
		break
	if n > guess:
		print "guess is high "
	elif n < guess:
		print "guess is low"
