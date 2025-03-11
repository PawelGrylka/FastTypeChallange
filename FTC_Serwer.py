import socket
import requests

def getServerIP() :
    url = "https://api64.ipify.org"
    payload = {"key": "value"}  # Corrected payload
    response = requests.get(url, params=payload)
    print(f"API Response: {response.text}")

def serverStart() :
    server_socket = socket.socket()
    port = 12345
    server_socket.bind(('127.0.0.1', port))
    server_socket.listen(1)

    print(f"Server is running on port {port}")

# Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    conn.send(b"Hello from the server!")
    conn.close()

# Socket client
    client_socket = socket.socket()
    try:
        client_socket.connect(('0.0.0.0', port))
    except ConnectionRefusedError as e:
        print(f"Connection failed: {e}")
    client_socket.close()

getServerIP()
serverStart()