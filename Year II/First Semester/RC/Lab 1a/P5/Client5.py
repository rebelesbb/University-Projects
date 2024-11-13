# Un client trimite unui server un numar.
# Serverul va returna clientului sirul divizorilor acestui numar.

import socket

def main():
    TCP_IP = '172.30.253.153'
    TCP_PORT = 8888
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    # 16 => 1 2 4 8 16

    num = input('Introduceti numarul: ')
    s.send(num.encode())

    divisors = s.recv(BUFFER_SIZE).decode().split('#')
    divisors = sorted([int(div) for div in divisors])

    for div in divisors:
        print(div)

    s.close()



if __name__ == '__main__':
    main()
