from socket import *
from json import loads

class ClientBroadcast:
    def __init__(self, PORT = 50000):
        self.serverPort = PORT
        self.serverSocket = socket(AF_INET, SOCK_DGRAM)
        self.serverSocket.bind(('', self.serverPort))
        #print ("The server is ready to receive")
        
    def listen(self):
        # TODO realizar verificação do servidor (se servidor for válido...)
        while 1:
            message, clientAddress = self.serverSocket.recvfrom(2048)
            message = loads(message)
            return (message['ip_server'], message['hostname'], message['PORT'])


if __name__ == '__main__':
    b = ClientBroadcast()
    b.listen()



"""
print(message, clientAddress)
modifiedMessage = message.upper()
self.serverSocket.sendto(modifiedMessage, clientAddress)
"""

#OK