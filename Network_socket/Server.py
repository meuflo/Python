import socket

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()

print(f"Waiting for connection on {HOST_IP}, port {HOST_PORT}")
connection_socket, client_adress = s.accept()
print(f"Connection established with {client_adress}")

while True:
    text_send = input("Vous : ")
    connection_socket.send(text_send.encode()) #.encode() transforme une chaine de caractere en byte donc en octet
    data_received = connection_socket.recv(MAX_DATA_SIZE)
    if not data_received:
        break
    print("Message : ", data_received.decode())


s.close()
connection_socket.close()