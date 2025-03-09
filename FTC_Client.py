import random
import threading
import socket
import Language


# s = socket.socket()
# port = 12345
# s.bind(('127.0.0.1', port))
# s.listen(1)  # Allow one client to connect


slowa = ["Test", "jeden", "dwa", "trzy"]

languageInput = input("Select Language")


class menu :
    def __init__(self,languageSelected,languages):
        self.languageSelected = languageSelected
        self.menuElements = languages[languageSelected]

    def showMenu(self):
        print(f"1.{self.menuElements["firstElementMenu"]}")
        print(f"2.{self.menuElements["secondElementMenu"]}")
        print(f"3.{self.menuElements["thirdElementMenu"]}")




menuInstance = menu("EN",Language.languages)
print(menuInstance.menuElements)

menuInstance.showMenu()


while True :
    userInput = input("What to DO")
    if userInput == "1" :
        print(f"{menuInstance.menuElements["menuSelect"]} : {menuInstance.menuElements["firstElementMenu"]}")
    if userInput == "2" :
        print(f"{menuInstance.menuElements["menuSelect"]} : {menuInstance.menuElements["secondElementMenu"]}")
    if userInput == "3" :
        print(f"{menuInstance.menuElements["menuSelect"]} : {menuInstance.menuElements["thirdElementMenu"]}")
        break





class GameLogic :
    def __init__(self,Player1):
        self.Player1 = Player1
        # self.Player2 = Player2
        self.timeIsOver = False
        self.score = 0

    def setRandomWord(self):
        randomnum = random.randrange(0, len(slowa))
        return slowa[randomnum]


    def mojTimer(self):
        global timeIsOver
        print("Czas minął!")
        timeIsOver = True


    def startGame(self):
        global timeIsOver, score

        wordToGuess = self.setRandomWord()
        timer = threading.Timer(5, self.mojTimer)
        timer.start()


        while not timeIsOver:
            print(f"Przepisz to słowo: {wordToGuess}")
            if input() == wordToGuess:
                score += 1
                print(f"Dobrze! Wynik: {score}")
                wordToGuess = self.setRandomWord()
            else:
                print("Źle, spróbuj ponownie!")

        print(f"Koniec gry! Twój wynik to: {score}")

