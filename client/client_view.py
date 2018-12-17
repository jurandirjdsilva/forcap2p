from client_broadcast import ClientBroadcast
from server import ServerInfo
from TCPClient import Client

def search_servers():
    b = ClientBroadcast()
    ip_server, hostname, server_port = b.listen()
    server = ServerInfo(server_name=hostname, ip_server=ip_server, server_port=server_port)
    return server

def read_letter(message):
    print('     Missed letters:')
    print('     ', end='')
    print(*message['current_word'],sep='')
    print('     Guess a letter.')
    print('     ', end='')
    l = input()[0]
    return l

if __name__ == '__main__':
    server_info = search_servers()
    client = Client(server_info)


# TODO usar o código abaixo para fazer o envio das mensagens
"""
sentence = input('Input lowercase sentence:')
encoded_message = bytes(sentence, "utf-8")
clientSocket.send(encoded_message)
modifiedSentence = clientSocket.recv(1024)
print ('From Server: ', modifiedSentence)
clientSocket.close()
"""