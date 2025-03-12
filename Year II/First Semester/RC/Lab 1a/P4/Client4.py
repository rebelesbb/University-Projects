# Un client trimite unui server doua siruri de caractere ordonate. Serverul va interclasa cele doua siruri si va returna clientului sirul rezultat interclasat.
import socket

def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8888
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    string1 = "aeiou"
    string2 = "abcdefghijklmn"
    string3 = string1 + '#' + string2

    s.send(string3.encode('utf-8'))

    mergedString = s.recv(BUFFER_SIZE).decode('utf-8')

    print(f'Sirul rezultat in urma interclasarii:\n{mergedString}')

    s.close()

if __name__ == '__main__':
    main()
