from random import randint
guess_taken = 0
number = randint(1,30)
p = 6
print"you have only %d chances" % (p)
while guess_taken < 6:
	print('enter the guess value')
	guess = int(input())
	guess_taken = guess_taken + 1

	if guess == number:
		print "you are guess is correct"
		break

	if guess > number:
		print "your guess is high"

	if guess < number:
		print "your guess is low"

if guess == number:	
	guess_taken = str(guess_taken)
	print('number of chances takes :'+guess_taken )