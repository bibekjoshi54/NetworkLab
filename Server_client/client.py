from socket import *
serverName = '192.168.43.222'
serverPort = 1000
message = raw_input("Enter the message: ")
clientSocket = socket(AF_INET,SOCK_DGRAM)
clientSocket.sendto(message,(serverName,serverPort))
modifiedMessage, send_addr = clientSocket.recvfrom(2048)
print(modifiedMessage)
clientSocket.close()
