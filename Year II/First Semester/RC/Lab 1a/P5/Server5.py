import socket
import threading
from threading import Thread

x = 0

def handle_client(conn, lock):

    num = int(conn.recv(1024).decode())

    global x
    for i in range(num):
        lock.lock()
        x += 1

    conn.send(str(x).encode())

    conn.close()


def divisors(num : int) -> str:
    divs = f'1#{num}'

    d=2

    while d * d <= num:
        if num % d == 0:
            if d * d != num:
                divs += f'#{d}#{num//d}'
            else:
                divs += f'#{d}'
        d += 1

    return divs


def main():
    TCP_IP = '172.30.253.51'
    TCP_PORT = 8888

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(5)

    clints = 20
    while True:
        conn, addr = s.accept()
        client_handler = threading.Thread(target=handle_client, args=(conn,))
        client_handler.start()
        clints -= 1
        if clints == 0:
            break

    s.close()

if __name__ == '__main__':
    main()

