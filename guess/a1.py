import random
n = random.randint(1,10)
n1 = random.randint(1,10)
print('what is '+ str(n) + ' + '+ str(n1)+'?')
answer = input()
if answer == n + n1:
	print ('correct')
else:
	print('Nope the answer is '+ str(n + n1))