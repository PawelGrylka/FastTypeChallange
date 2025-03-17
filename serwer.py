import socket
import threading
import random
from Words import words

game_words = words["PL"]

class GameSession:
    def __init__(self, conn1, conn2):
        self.conn1 = conn1
        self.conn2 = conn2
        self.scores = {1: 0, 2: 0}
        self.game_active = True

    def send_to_both(self, message):
        self.conn1.sendall(message.encode())
        self.conn2.sendall(message.encode())

    def handle_player(self, conn, player_id):
        while self.game_active:
            word = random.choice(game_words)
            conn.sendall(f"Przepisz to słowo: {word}\n".encode())
            try:
                data = conn.recv(1024).decode().strip()
                if data == word:
                    self.scores[player_id] += 1
                    conn.sendall("Dobrze!\n".encode())
                else:
                    conn.sendall("Źle, spróbuj ponownie!\n".encode())
            except:
                self.game_active = False
                break

    def start(self):
        self.send_to_both("Gra się rozpoczyna!\n")
        thread1 = threading.Thread(target=self.handle_player, args=(self.conn1, 1))
        thread2 = threading.Thread(target=self.handle_player, args=(self.conn2, 2))
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        self.send_to_both(f"Koniec gry! Wyniki: Gracz 1 - {self.scores[1]}, Gracz 2 - {self.scores[2]}\n")
        self.conn1.close()
        self.conn2.close()

class Server:
    def __init__(self, host='0.0.0.0', port=12347):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Serwer uruchomiony na {self.host}:{self.port}, czekam na graczy...")

    def wait_for_players(self):
        print("Oczekiwanie na gracza 1...")
        conn1, addr1 = self.server_socket.accept()
        print(f"Gracz 1 połączony z {addr1}")
        conn1.sendall("Oczekiwanie na drugiego gracza...\n".encode())

        print("Oczekiwanie na gracza 2...")
        conn2, addr2 = self.server_socket.accept()
        print(f"Gracz 2 połączony z {addr2}")
        conn2.sendall("Obaj gracze są połączeni, rozpoczynamy grę!\n".encode())

        game_session = GameSession(conn1, conn2)
        game_session.start()

if __name__ == "__main__":
    server = Server()
    server.wait_for_players()
