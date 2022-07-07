import socket
import json
import datetime

IP = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER = 256

header = {
  "to": IP,
  "from":IP,
  "data_length": 0,
  "timestamp":0
}

client = socket.socket()
client.connect((IP, PORT))
print(f"[CONNECTED] Conectado al servidor en {IP}")

while True:
  
  msg = input("Ingrese un mensaje: ")
  msg_len = len(msg)
  #print(f"[SERVER] Servidor dice: {msg}")
  header["data_lenght"]= msg_len
  header["timestamp"]= str(datetime.datetime.now())
  header = str(json.dumps(header))
  L = len(header)
  head = str(header) + " " * (HEADER - L)
  client.send(head.encode('utf-8'))
