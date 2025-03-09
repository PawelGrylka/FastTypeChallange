import random
import threading
import socket
import Language


# s = socket.socket()
# port = 12345
# s.bind(('127.0.0.1', port))
# s.listen(1)  # Allow one client to connect


slowa = ["Test", "jeden", "dwa", "trzy"]
timeIsOver = False
score = 0


languageInput = input("Select Language")


class menu :
    def __init__(self,languageSelected,languages):
        self.languageSelected = languageSelected
        self.menuElements = languages[languageSelected]

    def showMenu(self):
        print(self.menuElements["firstElementMenu"])
        print(self.menuElements["secondElementMenu"])
        print(self.menuElements["thirdElementMenu"])




menuInstance = menu("PL",Language.languages)
print(menuInstance.menuElements)

menuInstance.showMenu()

# def showMenu () :
#     print(firstELementMenu)
#     print(secondElementMenu)
#     print(thirdElementMenu)


while True :
    userInput = input("What to DO")
    if userInput == "1" :
        print("Wybrales opcje1")
    if userInput == "2" :
        print("Wybrales Opcje 2")
    if userInput == "3" :
        print("Wybrales Opcje 3")
        break










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

