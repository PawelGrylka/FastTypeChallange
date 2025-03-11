import socket
import requests

url = "https://api64.ipify.org"

payload = {"key","value"}

respone = requests.get(url, json =payload)


s = socket.socket()
port = 12345
s.bind(('127.0.0.1', port))
s.listen(1)  # Allow one client to connect

print(f"Server is running on port {port}")

conn, addr = s.accept()
print(f"Connected by {addr}")
conn.send(b"Hello from the server!")
conn.close()

try:
    s.connect(('127.0.0.1', port))
except ConnectionRefusedError as e:
    print(f"Connection failed: {e}")
