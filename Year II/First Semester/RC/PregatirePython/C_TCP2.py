import socket

def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8888

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    inputString = input('Introduceti sirul de caractere:\n>')

    s.send(inputString.encode())

    spacesCount = s.recv(1024).decode()
    print(f'Numarul de caractere spatiu din sirul trimis este {spacesCount}')

if __name__ == '__main__':
    main()
