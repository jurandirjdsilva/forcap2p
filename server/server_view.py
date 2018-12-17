from TCPServer import Server
from server_broadcast import ServerBroadcast
import time
from client import Client

class ServerView:
    def __init__(self,):
        self.server = Server()
        self.Clients = []
        self.build()
        self.open_connections() # estabelecer conexões
        self.run()

    def build(self,):
        self.state = {
            'current_word': None,
            'target_word': None,
            'level': None,
            'tip': None,
            'last_moves': []
        }
        self.message = {
            'current_word': None,
            'tip': None,
            'level': None
        }

    def open_connections(self,):
        brdcst = ServerBroadcast(server_ip=self.server.ip_address, 
            server_hostname=self.server.hostname, 
            PORT=50000, serverPORT=self.server.serverPort)
        print('# This Server #')
        print(f'    Hostname: {self.server.hostname}')
        print(f'    IP address: {self.server.ip_address}')
        print('Waiting by connections...')
        print('---------------- Clients ----------------')
        
        while len(self.Clients) < 2:

            for _ in range(5):
                brdcst.send()
                t_end = time.time() + 5 # 5 segundos para clientes se conectarem
                while time.time() < t_end:
                    try:
                        connectionSocket, addr = self.server.serverSocket.accept()
                    except:
                        continue
                    client = Client(connectionSocket=connectionSocket, addr=addr)
                    print(client.connectionSocket, client.addr)
                    self.Clients.append(client)
        time.sleep(1)

        print('----------------------------------------')
        
    def run(self,):
        # alterar
        while 1:
            connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(1024)
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence)
            connectionSocket.close()

if __name__ == '__main__':
    s = ServerView()