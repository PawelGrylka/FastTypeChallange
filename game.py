from language import languages
from menu import Menu
from game_logic import GameLogic
from network import Client

def select_language():
    language_keys = list(languages.keys())
    while True:
        language_input = input("Select Language (PL/EN): ").upper()
        if language_input not in language_keys:
            print("Invalid language. Try again.")
        else:
            menu_instance = Menu(language_input, languages)
            menu_instance.show_menu()
            return menu_instance

if __name__ == "__main__":
    menu_instance = select_language()
    while True:
        user_input = input("Co chcesz zrobić? ")
        if user_input == "1":
            server_ip = input("Podaj IP serwera: ")
            client = Client(server_ip)
            client.connect()
        elif user_input == "2":
            game = GameLogic("Player1")
            game.start_game()
        elif user_input == "3":
            print("Wyjście z gry.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
