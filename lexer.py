from sly import Lexer

class SucketLexer(Lexer):
    tokens= {
    CREATE,
    SERVER,
    CONNECT, 
    RECEIVE, 
    SEND, 
    CLIENT, 
    CLOSE, 
    BIND, 
    LISTEN, 
    ACCEPT
    }

    #strings containing ignored char between tokens
    ignore= ' \t'
    # literals= 

    #Rules for Tokens
    CREATE   = r'create'
    SERVER   = r'server'
    CONNECT  = r'connect'
    RECEIVE  = r'receive'
    SEND     = r'send'
    CLIENT   = r'client'
    CLOSE    = r'close'
    BIND     = r'bind'
    LISTEN   = r'listen'
    ACCEPT   = r'accept'

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r"""
        \n+
        """
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print('Illegal character %s', t.value[0])
        t.lexer.skip(1)
        return t

