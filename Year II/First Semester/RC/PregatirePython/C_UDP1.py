import socket

def main():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 8888

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    string = input('Introduceti sirul de caractere:\n>')
    s.sendto(string.encode('utf-8'), (UDP_IP, UDP_PORT))

    mirroredString, addr = s.recvfrom(1024)
    print(f'Sirul oglindit este: {mirroredString.decode()}')

if __name__ == '__main__':
    main()