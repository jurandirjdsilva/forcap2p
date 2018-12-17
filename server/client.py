class Client:
    def __init__(self, connectionSocket, addr, hostname=None, ip_address=None):
        self.hostname = hostname
        self.ip_address = ip_address
        self.connectionSocket = connectionSocket
        self.addr = addr