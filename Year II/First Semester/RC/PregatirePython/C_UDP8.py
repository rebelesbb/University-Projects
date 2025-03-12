import socket

def main():
    UDP_IP = "127.0.0.1"
    UDP_PORT = 8888

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    num1 = input("num1 = ")
    num2 = input("num2 = ")

    nums = str(num1) + ';' + str(num2)
    s.sendto(nums.encode(), (UDP_IP, UDP_PORT))

    cmmdc, addr = s.recvfrom(1024)
    cmmmc, addr = s.recvfrom(1024)

    print(f'CMMDC: {cmmdc.decode()}\nCMMMC: {cmmmc.decode()}')

if __name__ == '__main__':
    main()