import socket

class Server_Init(object):
    def create_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Server Initialized')
        return self.socket

    def bind(self,s):
        port = int(input('Port: '))
        s.bind(('', port))
        print('Socket has been binded')

    def listen(self,s):
        print('Listening...')
        s.listen(10)

    def accept(self,s):
        clt, adr = s.accept()
        print('Connection Found')
        return clt, adr

    def send(self,connection):
        response = 'Successfully connected'
        connection.send(response.encode())
        print('Response sent')

    def close(self, s):
        s.close()
        print('Session terminated')
    
    
class Client_Init(object):  
    def create_socket(self):
        #Creates and returns a socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Client Initialized')
        return self.socket

    def connect(self,s):
        host = input('Host ip address: \n*for localhost type 127.0.0.1* ')
        port = int(input('Port: \n**************************************************************\n** To connect to the server you must use the same IP Address**\n**************************************************************'))
        try:
            s.connect((host, port))
            print('Connection has been established')
        except:
            if KeyboardInterrupt:
                print("\n ** Connection Interrupted **")
            else:
                print("Connection could not be established")

    def receive(self,s):
        print(s.recv(4096))

    def close(self,s):
        s.close()
        print('Client has been disconnected')
    