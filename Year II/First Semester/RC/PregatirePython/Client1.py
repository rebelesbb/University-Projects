import socket

IP = input("IP: ")
PORT = input("PORT: ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, int(PORT)))

num1 = input("n1 = ")
num2 = input("n2 = ")

s.send(num1.encode())
s.send(num2.encode())

udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.sendto(num1.encode(), (IP, int(PORT)))

sum_, addr = udpSocket.recvfrom(1024)
print(sum_.decode())