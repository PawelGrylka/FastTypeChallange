# FastTypeChallange
 A simple game in Python that shows which of you types faster.

 
Projekt: Gra LAN i Gra Lokalna
To jest przykładowy projekt gry w Pythonie, który zawiera dwie funkcjonalności:

Gra LAN – umożliwia komunikację między klientem a serwerem.
Gra Lokalna – prosta gra polegająca na przepisywaniu słów z licznikiem punktów i limitem czasowym.
Projekt podzielony jest na kilka modułów, co ułatwia organizację kodu i jego późniejszą modyfikację.

Jak uruchomić projekt
Wymagania:

Python 3.x
Moduły standardowe (socket, threading, random, time)
Uruchamianie serwera (LAN):

Otwórz terminal w katalogu projektu.
Uruchom serwer:
nginx
Kopiuj
Edytuj
python server.py
Serwer zacznie nasłuchiwać na porcie 12345.
Uruchamianie klienta (LAN):

Otwórz drugi terminal.
Uruchom klienta:
nginx
Kopiuj
Edytuj
python client.py
Podaj adres IP serwera, gdy zostaniesz o to poproszony.
Uruchamianie gry lokalnej:

Uruchom główny plik:
css
Kopiuj
Edytuj
python main.py
W menu wybierz opcję „Gra Lokalna” (opcja 2). Gra rozpocznie się, a Twoim zadaniem będzie przepisywanie wyświetlanych słów. Gra trwa 30 sekund.
Opis modułów
language.py
Zawiera słownik languages z tłumaczeniami menu na język polski i angielski. Dzięki temu menu jest łatwe do zmiany i rozszerzenia o kolejne języki.

menu.py
Klasa Menu odpowiada za wyświetlanie opcji menu. Na podstawie wybranego języka (PL lub EN) wyświetla odpowiednie napisy.

game_logic.py
Klasa GameLogic zawiera logikę gry lokalnej. Wylosuje słowo z listy i uruchamia licznik czasowy. Użytkownik ma 30 sekund na wpisywanie poprawnych słów.

server.py
Plik zawiera klasę Server, która tworzy serwer nasłuchujący na wszystkich interfejsach (0.0.0.0) na porcie 12345. Po nawiązaniu połączenia, serwer wysyła wiadomość powitalną i odbiera dane od klienta.

client.py
Plik zawiera klasę Client, która łączy się z serwerem LAN. Po nawiązaniu połączenia klient odbiera wiadomość powitalną od serwera i wysyła odpowiedź.

main.py
Główny plik aplikacji. Umożliwia wybór języka, a następnie wyświetla menu z opcjami:

Połącz z serwerem (klient LAN)
Gra Lokalna
Wyjdź z gry
