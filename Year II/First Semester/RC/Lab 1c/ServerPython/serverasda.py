import socket

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