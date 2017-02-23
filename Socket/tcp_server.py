from socket import *
serversocket = socket(AF_INET,SOCK_STREAM)
serversocket.bind(('',9000))
try:
    server = gethostname()
    server += ': '
    server= server.encode('UTF-8')
    serversocket.listen()
    client_socket, client_addr = serversocket.accept()
    print('Connection from ',client_addr)
    try:
        while 1:
            data = client_socket.recv(1024)
            print(data.decode("UTF-8"))
            data = input('>')
            client_socket.send(server + data.encode('UTF-8'))
            if not data: break
    except:
        print('Exception occured1')
        client_socket.close()
        serversocket.close()
except:
    print('Exception occured2')
    serversocket.close()
client_socket.close()
serversocket.close()