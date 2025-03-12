# Un client trimite unui server un sir de caractere. Serverul va returna clientului numarul de caractere spatiu din sir.
import socket

def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8888
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    str_ = input("Introduceti sirul de caractere:\n>")
    s.send(str_.encode())

    spaces = s.recv(BUFFER_SIZE).decode('utf-8')
    print(f'Sirul contine {spaces} spatii.')

    s.close()

if __name__ == '__main__':
    main()
