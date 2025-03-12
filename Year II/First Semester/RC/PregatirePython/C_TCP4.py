import socket

def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8888

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    string1 = input("Introduceti primul sir de caractere\n>")
    string2 = input("Introduceti al doilea sir de caractere\n>")

    s.send(string1.encode())
    s.send(string2.encode())

    mergedString = s.recv(1024)
    print(mergedString.decode())

if __name__ == '__main__':
    main()

