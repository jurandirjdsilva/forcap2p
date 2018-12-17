from socket import *

class Client():
    def __init__(self,server):
        self.ip_server = server.ip_server
        self.serverPort = server.server_port
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect((self.ip_server,int(self.serverPort)))



"""
sentence = input('Input lowercase sentence:')
encoded_message = bytes(sentence, "utf-8")
clientSocket.send(encoded_message)
modifiedSentence = clientSocket.recv(1024)
print ('From Server: ', modifiedSentence)
clientSocket.close()
"""