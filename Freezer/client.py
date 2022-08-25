import socket
import sys

HOST = '10.125.24.84'    # The remote host
PORT =  12000         # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
server = True

while server:
    msg=input("message to send: ")
    if msg == "":
        msg = "list"
    s.sendall(msg.encode())
    data = s.recv(1024)
    print('Received', data.decode())
    if msg == "quit()" :
        break
s.close()