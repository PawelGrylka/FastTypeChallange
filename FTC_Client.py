import random
import threading

slowa = ["Test", "jeden", "dwa", "trzy"]
timeIsOver = False
score = 0


def setRandomWord():
    randomnum = random.randrange(0, len(slowa))
    return slowa[randomnum]


def mojTimer():
    global timeIsOver
    print("Czas minął!")
    timeIsOver = True


def startGame():
    global timeIsOver, score

    wordToGuess = setRandomWord()
    timer = threading.Timer(5, mojTimer)
    timer.start()

    while not timeIsOver:
        print(f"Przepisz to słowo: {wordToGuess}")
        if input() == wordToGuess:
            score += 1
            print(f"Dobrze! Wynik: {score}")
            wordToGuess = setRandomWord()
        else:
            print("Źle, spróbuj ponownie!")

    print(f"Koniec gry! Twój wynik to: {score}")

# Uruchomienie gry
startGame()