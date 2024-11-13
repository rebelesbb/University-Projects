import socket

def count_spaces(str_ : str) -> int:
    spaces = 0
    for char in str_:
        if char == ' ':
            spaces += 1
    return spaces


def main():
    TCP_IP = "127.0.0.1"
    TCP_PORT = 8888
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()

        str_ = conn.recv(BUFFER_SIZE).decode('utf-8')

        spaces = count_spaces(str_)
        print(f"S-au gasit {spaces} spatii in sirul primit.")

        conn.send(str(spaces).encode('utf-8'))
        conn.close()
        break
    s.close()

if __name__ == "__main__":
    main()