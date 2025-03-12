import socket
import requests
import time

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
    server_socket.bind(('0.0.0.0', port))  # Nasłuchiwanie na wszystkich interfejsach
    server_socket.listen(1)

    print(f"✅ Serwer działa na porcie {port} i czeka na połączenia...")

    conn, addr = server_socket.accept()
    print(f"🔗 Połączono z: {addr}")

    conn.send(b"Hello from the server!")
    conn.close()

# Uruchom klienta
def clientStart(server_ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 12345

    try:
        print(f"🔄 Próba połączenia z serwerem: {server_ip}:{port}...")
        client_socket.connect((server_ip, port))
        response = client_socket.recv(1024)
        print(f"📩 Odpowiedź serwera: {response.decode()}")
    except ConnectionRefusedError as e:
        print(f"❌ Połączenie nieudane: {e}")
    finally:
        client_socket.close()

# Uruchamianie serwera i klienta
server_ip = getServerIP()  # Pobierz publiczne IP
if server_ip:
    # Uruchom serwer w osobnym wątku (nie blokuje programu)
    import threading
    server_thread = threading.Thread(target=serverStart, daemon=True)
    server_thread.start()

    # Poczekaj chwilę, aby serwer zdążył wystartować
    time.sleep(2)

    # Uruchom klienta, który łączy się do uzyskanego IP
    clientStart(server_ip)
else:
    print("🚨 Nie można pobrać IP, klient nie zostanie uruchomiony.")
