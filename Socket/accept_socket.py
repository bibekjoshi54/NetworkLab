from socket import *

sock = socket(AF_INET,SOCK_STREAM)
sock.connect(('localhost', 8000))
gethostname()


