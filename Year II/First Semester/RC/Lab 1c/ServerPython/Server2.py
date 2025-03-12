import socket
import threading

def handleClient(conn: socket):
    num = int(conn.recv(1024).decode())

    isPrime = True
    if num < 2:
        isPrime = False
    elif num == 2:
        isPrime = True
    elif num % 2 ==0:
        isPrime = False
    else:
        d = 3
        while d * d <= num:
            if num % d == 0:
                isPrime = False

    if isPrime:
        conn.send('1'.encode())
    else:
        conn.send('0'.encode())

    conn.close()
    conn.close()


def main():
    print('Server starting...')
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8888
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)
        break

    s.close()

if __name__ == '__main__':
    main()


