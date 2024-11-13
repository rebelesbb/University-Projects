import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

gameId = s.recv(1024).decode()
print(gameId)

letter = s.recv(1024).decode()
print(letter)
isYourTurn = s.recv(1024).decode()
print("Is your turn?" + isYourTurn)
if isYourTurn.count('Y'):
    isYourTurn = True
else:
    isYourTurn = False

while True:
    if isYourTurn:
        word = input('Enter a word: ')
        s.send(word.encode())
        isYourTurn = False
    else:
        word = s.recv(1024).decode()
        print("Cuvant dat de player 2: " + word)
        isYourTurn = True


s.close()

# firstLetter = s.recv(1024)
# print(firstLetter)
#
# while True:
#     s.recv(1024)