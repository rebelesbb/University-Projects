import socket


def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8888

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    numCount = int(input('n = '))
    s.send(str(numCount).encode())
    for i in range(numCount):
        num = input(f'Numar {i + 1} = ')
        s.send(num.encode())

    suma = s.recv(1024).decode()
    print(suma)

if __name__ == '__main__':
    main()

