p = 17
q = 5
c=0
while p > q:
	p -= q
	c+=1
print p,c


"""hangman
name = raw_input("What is your name? ")
print "Hello, " + name, "Time to play hangman!"
print "\n"
print "Start guessing..."
word = "kumar"
guesses = ''
turns = 10
while turns > 0:         
    failed = 0               
    for char in word:      
        if char in guesses:    
            print char,    
        else:
            print "_",     
            failed += 1    
    if failed == 0:        
        print "\nYou won" 
        break              
    guess = raw_input("guess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print "Wrong\n"    
        print "You have", + turns, 'more guesses' 
        if turns == 0:           
            print "You Loose\n"  