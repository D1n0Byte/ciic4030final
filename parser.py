from Sockets_Init import Server_Init as Server
from Sockets_Init import Client_Init as Client
from sly import Parser
from lexer import SucketLexer
import sys

class SucketParser(Parser): 
    tokens = SucketLexer.tokens
    
    def __init__(self):
        self.gCommands = { }
        self.cSocket = None
        self.cSocket = None
        self.tSocket = None
    
    @_('CREATE CLIENT')
    def p_create_client(self,p):
        self.cSocket = Client.create_socket(self)
        self.gCommands[p.CLIENT] = self.cSocket 

    @_('CREATE SERVER')
    def p_create_server(self,p):
        self.sSocket = Server.create_socket(self)
        self.gCommands[p.SERVER] = self.sSocket

    @_('CONNECT')
    def p_connect(self,p):
        Client.connect(self.cSocket)

    @_('RECEIVE')
    def p_receive(self,p):
        Client.receive(self.cSocket)

    @_('SEND')
    def p_send(self,p):
        self.tSocket = Server.create_socket(self)
        Server.send(self.tSocket)

    @_('CLIENT CLOSE')
    def p_client_close(self,p):
        Client.close(self.cSocket)

    @_('BIND')
    def p_bind(self,p):
        'bind : BIND'
        Server.bind(self.sSocket)

    @_('LISTEN')
    def p_listen(self,p):
        Server.listen(self.sSocket)

    @_('ACCEPT')
    def p_accept(self,p):
        'accept : ACCEPT'
        return Server.accept(self.sSocket)

    @_('SERVER CLOSE')
    def p_server_close(self,p):
        Server.close(self.sSocket)
        
        
if __name__ == '__main__':
    lexer = SucketLexer()
    parser = SucketParser()
    while True:
        try:
            msg = input('SuckET > ')
            if msg == 'exit':
                sys.exit()
        except EOFError:
            break
        if msg:
            parser.parse(lexer.tokenize(msg))