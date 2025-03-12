import socket
import sys
from datetime import datetime


# the ip and port are given from the command prompt

def main():
    if len(sys.argv) < 2:
        print('Numar insuficient de argumente\nUtilizare: program.py adresaIP port')
        sys.exit()
    else:
        UDP_IP = sys.argv[1]
        UDP_PORT = sys.argv[2]

        print("UDP target IP:", UDP_IP)
        print("UDP target port:", UDP_PORT)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.sendto('Cerere data'.encode(), (UDP_IP, int(UDP_PORT)))
    print('Cerere trimisa la server.\nSe asteapta raspuns...')

    secondsFromDate, addr = s.recvfrom(1024)
    secondsFromDate = int(secondsFromDate.decode())
    print(f'Valoare primita: {secondsFromDate}')

    currentDate = datetime.fromtimestamp(secondsFromDate).strftime('%d/%m/%Y')

    print(f"Data curenta este :  {currentDate}")


if __name__ == "__main__":
    main()