import random
import threading

class GameLogic:
    def __init__(self, player_name):
        self.player_name = player_name
        self.time_is_over = False
        self.score = 0
        self.words = ["Test", "jeden", "dwa", "trzy"]

    def set_random_word(self):
        return random.choice(self.words)

    def timer(self):
        print("Czas minął!")
        self.time_is_over = True

    def start_game(self):
        word_to_guess = self.set_random_word()
        # Uruchom timer na 30 sekund
        timer_thread = threading.Timer(30, self.timer)
        timer_thread.start()

        while not self.time_is_over:
            print(f"Przepisz to słowo: {word_to_guess}")
            if input() == word_to_guess:
                self.score += 1
                print(f"Dobrze! Wynik: {self.score}")
                word_to_guess = self.set_random_word()
            else:
                print("Źle, spróbuj ponownie!")

        print(f"Koniec gry! Twój wynik to: {self.score}")
