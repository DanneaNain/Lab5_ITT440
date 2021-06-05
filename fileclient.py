import socket
import sys

if (len(sys.argv) > 1):
    ServerIp = sys.argv[1]
else:
    print(" python3 fileserver.py < server ip address > \n\n")
    exit(1)


s = socket.socket()

port = 9999

s.connect((ServerIp, port))


filetoSend = input('\nPlease enter the file name that want to be stored in the server: ')
s.send(filetoSend.encode())
file = open(filetoSend, "rb")

SendData = file.read(99999)

while SendData:

    print("\nReceiving some message from the server:", s.recv(1024).decode("utf-8"))
    
    s.send(SendData)
    SendData = file.read(99999)
    print("This " + filetoSend + " file are succesfully copied to the server for storage.\n")
    
s.close()
