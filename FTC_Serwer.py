import socket
import requests
import time
import threading

# Pobierz publiczne IP serwera
def getServerIP():
    url = "https://api64.ipify.org"
    try:
        response = requests.get(url)
        response.raise_for_status()
        server_ip = response.text.strip()
        print(f"🌍 Twoje publiczne IP: {server_ip}")
        return server_ip
    except requests.RequestException as e:
        print(f"❌ Błąd przy pobieraniu IP: {e}")
        return None

# Uruchom serwer
def serverStart():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    port = 12345

    try:
        server_socket.bind(('127.0.0.1', port))  # Nasłuchiwanie na wszystkich interfejsach
        server_socket.listen(1)
        print(f"✅ Serwer działa na porcie {port} i czeka na połączenia...")

        conn, addr = server_socket.accept()  # Czekaj na połączenie
        print(f"🔗 Połączono z: {addr}")

        # Wysyłanie wiadomości
        conn.send(b"Hello from the server!")

        # Odbieranie wiadomości od klienta
        data = conn.recv(1024)
        if data:
            print(f"📩 Odebrano dane: {data.decode()}")

        # Zamykanie połączenia
        conn.close()

    except Exception as e:
        print(f"❌ Błąd uruchamiania serwera: {e}")

# Uruchom klienta
def clientStart(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 12345

    try:
        print(f"🔄 Próba połączenia z serwerem: {server_ip}:{port}...")
        client_socket.connect((server_ip, port))  # Łączenie się z serwerem

        # Odbieranie wiadomości od serwera
        response = client_socket.recv(1024)
        print(f"📩 Odpowiedź serwera: {response.decode()}")

        # Wysyłanie wiadomości do serwera
        client_socket.send(b"Hello from the client!")

    except ConnectionRefusedError as e:
        print(f"❌ Połączenie nieudane: {e}")
    finally:
        client_socket.close()

# Uruchamianie serwera i klienta
def startServerAndClient():
    server_ip = getServerIP()  # Pobierz publiczne IP
    if server_ip:
        # Uruchom serwer w osobnym wątku (nie blokuje programu)
        server_thread = threading.Thread(target=serverStart, daemon=True)
        server_thread.start()

        # Poczekaj chwilę, aby serwer zdążył wystartować
        time.sleep(2)

        # Uruchom klienta, który łączy się do uzyskanego IP
        clientStart(server_ip)
    else:
        print("🚨 Nie można pobrać IP, klient nie zostanie uruchomiony.")

serverStart()