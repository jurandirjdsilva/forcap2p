from socket import *
from collections import namedtuple

Move = namedtuple('Move', 'player letter')
setdefaulttimeout(1)

class Server:
    def __init__(self,):
        self.serverPort = 12000
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.bind(('', self.serverPort))
        self.serverSocket.listen(1)
        self.hostname = gethostname()
        self.ip_address = gethostbyname(self.hostname)


