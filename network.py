import socket
import threading

class Server:
    def __init__(self, host='0.0.0.0', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Serwer działa na {self.host}:{self.port}, czeka na połączenia...")

        while True:
            conn, addr = self.server_socket.accept()
            print(f"Połączono z {addr}")
            threading.Thread(target=self.handle_client, args=(conn,), daemon=True).start()

    def handle_client(self, conn):
        try:
            conn.send(b"Witaj na serwerze!")
            data = conn.recv(1024)
            if data:
                print(f"Odebrano: {data.decode()}")
        except Exception as e:
            print(f"Błąd podczas obsługi klienta: {e}")
        finally:
            conn.close()

class Client:
    def __init__(self, server_ip, port=12345):
        self.server_ip = server_ip
        self.port = port

    def connect(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((self.server_ip, self.port))
            print("Połączono z serwerem!")
            response = client_socket.recv(1024)
            print(f"Serwer mówi: {response.decode()}")
            client_socket.send(b"Hello from client!")
        except Exception as e:
            print(f"Błąd połączenia: {e}")
        finally:
            client_socket.close()
