import socket
class Client:
    def __init__(self,serverIp, port):
        self.localHost = serverIp
        self.port = port
        self.c = socket.socket()
        self.c.connect((self.localHost, self.port))


    def sendData(self,name):
       self.c.send(bytes(name,'utf-8'))


if __name__ == '__main__':
    b = Client('localhost',9999)
    b.sendData('harsh')
