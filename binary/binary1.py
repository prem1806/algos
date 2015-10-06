import random
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
     # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

word = getRandomWord(words)
print "Hello, Rohit  play hangman!"
print "\n"
print "Start guessing..."
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
            print "the word is %s" %(word) 
