from socket import *

client = socket(AF_INET,SOCK_STREAM)
myname = gethostname()
myname += ': '
myname = myname.encode('UTF-8')
client.connect(('47.247.2.172' ,8001))
while 1:
    data = input('>')
    if not data: break
    data = data.encode('UTF-8')
    client.send(myname + data)
    print(client.recv(1024).decode("UTF-8"))
client.close()
client.close()