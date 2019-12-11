from sly import lexer

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
    # ignore=
    # literals= 
