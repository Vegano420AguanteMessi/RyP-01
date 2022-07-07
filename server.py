import socket
import json

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER = 256

server = socket.socket()
server.bind((IP, PORT))
server.listen()
print(f"[LISTENING] El servidor esta esperando conexiones en {IP}")

conn, addr = server.accept()
print(f"[CONNECTED] Nueva conexion en {addr}")

while True:
  header = conn.recv(HEADER)
  header = json.loads(header)
  print(header) 
  #lenght = header ["lenght"]
