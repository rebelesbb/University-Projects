import socket
import sys


def main():
    if len(sys.argv) < 2:
        print('Insufficient arguments')
        sys.exit()

    TCP_IP = sys.argv[1]
    TCP_PORT = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    numArrayOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numArrayTwo = [1, 2, 3, 4, 5, 20, 21, 22, 23, 24]

    arrayString = ''
    for num in numArrayOne:
        arrayString += str(num) + ','

    arrayString += ';'

    for num in numArrayTwo:
        arrayString += str(num) + ','

    s.send(arrayString.encode())

    print('Data sent to server\nWaiting for response...')

    numsRequested = s.recv(1024).decode()
    print(f'Numbers returned by the server:\n{numsRequested}')

if __name__ == '__main__':
    main()