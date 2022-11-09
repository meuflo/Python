import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024


print(f"Connection to the server {HOST_IP}, port {HOST_PORT}")

while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP,HOST_PORT))
    except ConnectionRefusedError:
        print("ERROR : Unable to connect to the server. Reconnect...")
        time.sleep(1)
    else:
        print("Connected to the server")
        break

while True:
        data_received = s.recv(MAX_DATA_SIZE)
        if not data_received:
            break
        print("Message : ", data_received.decode())
        text_send = input("Vous : ")
        s.send(text_send.encode())


s.close