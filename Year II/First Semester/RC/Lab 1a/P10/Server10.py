import socket
import string
from string import ascii_lowercase


def count_appearance(string1: string, string2: string) -> string:

    letters = {letter: 0 for letter in ascii_lowercase}
    letters[' '] = 0

    for pos in range(min(len(string1), len(string2))):
        if string1[pos] == string2[pos]:
            letters[string1[pos].lower()] += 1

    maxLetter = 'a'

    for letter in letters.keys():
        if letters.get(letter) > letters.get(maxLetter):
            maxLetter = letter

    return maxLetter

def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8888
    BUFF_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP,TCP_PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print("Connected by ", addr)

        string1, string2 = conn.recv(BUFF_SIZE).decode().split('#')

        maxLetter = count_appearance(string1, string2)
        conn.send(maxLetter.encode())

        conn.close()
        break

    s.close()

if __name__ == '__main__':
    main()