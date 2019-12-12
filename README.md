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
- Data
  - regex: `\".*\"`
- Integers
  - regex: `\d+`
- Equal
  - regex: `=`
- String
  - regex: `[a-zA-Z_.-][a-zA-Z0-9_.-]*`
- Reserverd Keywords
   ```Javascript
    {
        'create' : 'CREATE', 
        'server' : 'SERVER', 
        'client' : 'CLIENT', 
        'delete' : 'DELETE', 
        'connect' : 'CONNECT', 
        'send' : 'SEND', 
        'info' : 'INFO' 
    }
  ```
## Grammar
```
statement : CREATE CLIENT STRING | DELETE CLIENT STRING | DELETE SERVER STRING
statement : CREATE SERVER STRING DATA INT | CREATE SERVER STRING STRING INT | CREATE SERVER STRING
statement : INFO STRING
statement : STRING EQUALS DATA | STRING EQUALS INT
statement : STRING SEND STRING DATA | STRING SEND STRING STRING
statement : STRING CONNECT STRING | STRING CONNECT DATA
```
This grammar could be also represented in a more convenient way using the following sequence:
```
statement : CREATE CLIENT STRING | DELETE CLIENT STRING | DELETE SERVER STRING | CREATE SERVER STRING DATA INT | CREATE SERVER STRING STRING INT | CREATE SERVER STRING | INFO STRING | STRING EQUALS DATA | STRING EQUALS INT | STRING SEND STRING DATA | STRING SEND STRING STRING | STRING CONNECT STRING | STRING CONNECT DATA
```
## Operations
- **Create**
    - `create server myserver "ip_addr" port_nbr`
    - `create client myclient`
- **Delete**
    - `delete server myserver`
    - `delete client myclient`
- **Local Connection**
    - `myclient connect myserver`
- **External Connection**
    - `myclient connect "addr_external_server"`
        - Example: `myclient connect "https://www.google.com"`
        *NOTE: "https://www.google.com" === "172.217.8.132"*
- **Data Processing**
    - `myclient send myserver "data or message"`
    - `myserver1 send myserver2 "data or message"`
- **Info**
    - `info myserver`
    - `info myclient`
- **Variables**
    - `var1 = "some string"`