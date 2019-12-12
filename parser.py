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
        self.sSocket = None
        self.tSocket = None
    
    #Create the client
    @_('CREATE CLIENT')
    def statement(self,p):
        self.cSocket = Client.create_socket(self)
        self.gCommands[p.CLIENT] = self.cSocket 
        return self.cSocket

    #Create the Server
    @_('CREATE SERVER')
    def statement(self,p):
        self.sSocket = Server.create_socket(self)
        self.gCommands[p.SERVER] = self.sSocket
        return self.sSocket

    @_('CONNECT')
    def statement(self,p):
        Client.connect(self, self.cSocket)

    @_('RECEIVE')
    def statement(self,p):
        Client.receive(self, self.cSocket)

    @_('SEND')
    def statement(self,p):
        self.tSocket = Server.create_socket(self)
        Server.send(self, self.tSocket)
        Client.receive(self.cSocket)

    @_('CLIENT CLOSE')
    def statement(self,p):
        Client.close(self, self.cSocket)

    @_('SERVER CLOSE')
    def statement(self,p):
        Server.close(self, self.sSocket)
        
    @_('CLOSE CONNECTIONS')
    def statement(self,p):
        Client.close(self, self.cSocket) 
        Server.close(self,self.sSocket)
        
    @_('BIND')
    def statement(self,p):
        'bind : BIND'
        Server.bind(self, self.sSocket)

    @_('LISTEN')
    def statement(self,p):
        Server.listen(self, self.sSocket)

    @_('ACCEPT')
    def statement(self,p):
        return Server.accept(self, self.sSocket)
        
        
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