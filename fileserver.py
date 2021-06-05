import socket

s = socket.socket()

hostname = socket.gethostname() 
ip_addr = socket.gethostbyname(hostname) 

port = 9999
print("IP address of the server: ", ip_addr)
print("The server is listening on port: ", port)
print("Waiting for a connection from client....")

s.bind(('', port))

s.listen(5)

while True:

    c, addr = s.accept()

    message = "\n\nHi, Client! Your ip addresss is "+ addr[0] + " \nThank you because trust us to store the file. \nDon't Worry, the files are safe with us."    
    c.send(message.encode())

    filename = c.recv(1024).decode("utf-8")
    file = open(filename, "wb")

    receiveData = c.recv(99999)

    while receiveData:
        file.write(receiveData)
        receiveData = c.recv(99999)

    file.close()
    print("\nFile has been copied successfully \n")

    c.close()
    print("Server closed the connection \n")

    break
