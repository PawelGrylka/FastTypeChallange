import random

slowa = ["Test","jeden","dwa","trzy"]



score  = 0
randomnum = random.randrange(0,len(slowa))
print(randomnum)

def setRandomWord() :
    randomnum = random.randrange(0, len(slowa))
    randomWord = slowa[randomnum]
    print(randomWord)



while score < 2 :
    setRandomWord()
    score += 1







def checkWord(word):
    print(word)

def startGame() :

    return