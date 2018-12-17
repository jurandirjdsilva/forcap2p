# Send UDP broadcast packets
import sys, time
from socket import *

class ServerBroadcast:
    def __init__(self, server_ip, server_hostname, serverPORT, PORT=50000):
        self.MYPORT = PORT
        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.bind(('', 0))
        self.s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.message = '{' + f'"ip_server":"{server_ip}", "hostname":"{server_hostname}", "PORT":"{serverPORT}"' + '}'
        
    def send(self,):
        self.s.sendto(bytes(self.message.encode()), ('<broadcast>', self.MYPORT))

if __name__ == '__main__':
	#b = ServerBroadcast()
	#b.send()
    pass
