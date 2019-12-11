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
    CREATE   = 'create'
    SERVER   = 'server'
    CONNECT  = 'connect'
    RECEIVE  = 'receive'
    SEND     = 'send'
    CLIENT   = 'client'
    CLOSE    = 'close'
    BIND     = 'bind'
    LISTEN   = 'listen'
    ACCEPT   = 'accept'