import socket


def merge(string1: str, string2: str) -> str:
    i = 0
    j = 0
    mergedString = ""
    while i < len(string1) and j < len(string2):
        if string1[i] <= string2[j]:
            mergedString += string1[i]
            i += 1
        else:
            mergedString += string2[j]
            j += 1

    while i < len(string1):
        mergedString += string1[i]
        i += 1
    while j < len(string2):
        mergedString += string2[j]
        j += 1

    return mergedString


def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 8888
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print('Connected by', addr)

        """
        string1 = conn.recv(BUFFER_SIZE).decode('utf-8')
        print(string1)
        string2 = conn.recv(BUFFER_SIZE).decode('utf-8')
        print(string2)
        problema cred ca e ca am dat buff size 1024 iar 
        sirurile au fiecare mai putin de atat si atunci 
        toate datele se primesc la primul apel recv
        si al doilea ingheata 
        """

        string1, string2 = conn.recv(BUFFER_SIZE).decode('utf-8').split('#')


        print(f'Sirurile de caractere primite:\n{string1}\n{string2}\n')

        mergedString = merge(string1, string2)


        conn.send(mergedString.encode('utf-8'))
        conn.close()
        break

    s.close()


if __name__ == '__main__':
    main()
