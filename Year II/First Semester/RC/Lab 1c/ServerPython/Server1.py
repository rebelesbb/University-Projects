import socket

def doSum():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 8888

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    number1, addr = sock.recvfrom(1024)
    print(f"Number received from address {addr} : {number1}")

    number2, addr = sock.recvfrom(1024)
    print(f"Number received from address {addr} : {number2}")

    SUM = str(int(number1) + int(number2))
    print(SUM)
    sock.sendto(SUM.encode(), addr)

if __name__ == '__main__':
    doSum()

