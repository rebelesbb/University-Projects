import socket

TCP_IP = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, PORT))

s.send('7'.encode())

s.close()