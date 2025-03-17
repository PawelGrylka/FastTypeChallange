import random
import threading
import socket
import Language





slowa = ["Test", "jeden", "dwa", "trzy"]




class menu :
    def __init__(self,languageSelected,languages):
        self.languageSelected = languageSelected
        self.menuElements = languages[languageSelected]

    def showMenu(self):
        print(f"1.{self.menuElements["firstElementMenu"]}")
        print(f"2.{self.menuElements["secondElementMenu"]}")
        print(f"3.{self.menuElements["thirdElementMenu"]}")



def LanguageSelection():
    # Pobierz klucze języków bez zmieniania `Language.languages`
    languageKeys = list(Language.languages.keys())

    while True:  # Pętla dla wyboru języka
        languageInput = input("Select Language: ").upper()  # Pobranie języka od użytkownika
        if languageInput not in languageKeys:
            print("Invalid language. Try again.")  # Jeśli język jest nieprawidłowy, pytamy ponownie
        else:
            # Tworzenie obiektu menu w oparciu o wybrany język
            menuInstance = menu(languageInput, Language.languages)
            menuInstance.showMenu()  # Wyświetlenie menu
            return menuInstance  # Zwrócenie instancji menu

menuInstance = LanguageSelection()


class Player :
    def __init__(self,PlayerName):
        self.PlayerName = PlayerName



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

        wordToGuess = self.setRandomWord()
        timer = threading.Timer(30, self.mojTimer)
        timer.start()


        while not self.timeIsOver:
            print(f"Przepisz to słowo: {wordToGuess}")
            if input() == wordToGuess:
                self.score += 1
                print(f"Dobrze! Wynik: {self.score}")
                wordToGuess = self.setRandomWord()
            else:
                print("Źle, spróbuj ponownie!")

        print(f"Koniec gry! Twój wynik to: {self.score}")




class ServerOperations:
    def __init__(self):
        pass



    def connectToServer(self, host, port):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            print(f"Connected to server at {host}:{port}")
            return client_socket
        except ConnectionRefusedError as e:
            print(f"Connection failed: {e}")
            return None

    def enterIP(self):
        serverIPinput = input()
        connection = self.connectToServer(serverIPinput,12345)
        print("rozpoczeto probe polaczenia")
        if connection :

            #DODAC DO JEZYKA
            print("polaczone")
        else :
            print("Nie polaczono")




server = ServerOperations()


while True :
    userInput = input("What to DO")
    if userInput == "1" :
        print(f"{menuInstance.menuElements["menuSelect"]} : {menuInstance.menuElements["firstElementMenu"]}")
        server.enterIP()
    if userInput == "2" :
        print(f"{menuInstance.menuElements["menuSelect"]} : {menuInstance.menuElements["secondElementMenu"]}")
        game = GameLogic("Player1", )
        game.startGame()
    if userInput == "3" :
        print(f"{menuInstance.menuElements["menuSelect"]} : {menuInstance.menuElements["thirdElementMenu"]}")


    if userInput == "4" :
        print(f"{menuInstance.menuElements["menuSelect"]} : {menuInstance.menuElements["fourthElementMenu"]}")
        break