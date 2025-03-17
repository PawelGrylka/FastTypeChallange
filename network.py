import socket

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

if __name__ == "__main__":
    server_ip = input("Podaj IP serwera: ")
    client = Client(server_ip)
    client.connect()