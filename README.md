# CIIC4030 Project: SuckET Device Communications

Design a new programming language to simplify the communication between
devices: The new language must be declarative and functional and provide
simple functionality to create local servers and allow communication with
external servers. You must clearly define the syntax of the new language.

# Team Members

- María Cordero
- Julio Aguilar

# Description

The language will allow to perform basic creation of local servers and allow communication with servers.


# Language Structure

## Tokens
```
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
```
## Grammar
```
statement : CREATE CLIENT
statement : CREATE SERVER 
statement : ClOSE CLIENT
statement : CLOSE SERVER
statement : CONNECT
statement : SEND
statement : RECEIVE
statement : BIND
statement : LISTEN
statement : ACCEPT
```