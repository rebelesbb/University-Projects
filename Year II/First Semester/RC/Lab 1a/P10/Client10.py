# Un client trimite unui server doua siruri de caractere.
# Serverul ii raspunde clientului cu caracterul care se regaseste
# de cele mai multe ori pe pozitii identice in cele doua siruri
# si cu numarul de aparitii ale acestui caracter.

import socket

def main():
    TCP_IP = '172.30.253.153'
    TCP_PORT = 1234

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    string1 = "Ana are mere"
    string2 = "Ana are merisoare"

    s.send(f'{string1}#{string2}'.encode())
    maxLetter = s.recv(10).decode()
    print(f'Litera cu numarul de aparitii pe pozitii identice este: {maxLetter}')

    s.close()

if __name__ == '__main__':
    main()