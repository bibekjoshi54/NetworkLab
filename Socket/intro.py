from socket import *
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost',8000))
sock.listen(2)
cliaddr,addr = sock.accept()