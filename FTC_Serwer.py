import socket
import requests

# Pobierz IP serwera
def getServerIP():
    url = "https://api64.ipify.org"
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Twoje publiczne IP: {response.text}")
        return response.text
    except requests.RequestException as e:
        print(f"Błąd przy pobieraniu IP: {e}")

# Uruchom serwer
def serverStart():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 12345
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)

    print(f"✅ Serwer działa na porcie {port}")

    conn, addr = server_socket.accept()
    print(f"🔗 Połączenie od: {addr}")

    conn.send(b"Hello from the server!")
    conn.close()

# Uruchom klienta
def clientStart():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"  # Możesz tu wpisać IP serwera, jeśli jest w innej sieci.
    port = 12345

    try:
        client_socket.connect((server_ip, port))
        response = client_socket.recv(1024)
        print(f"📩 Odpowiedź serwera: {response.decode()}")
    except ConnectionRefusedError as e:
        print(f"❌ Połączenie nieudane: {e}")
    finally:
        client_socket.close()

# Uruchamianie
getServerIP()
serverStart()  # Uruchomi serwer
