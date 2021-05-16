import socket
class Server:
   def __init__(self,serverIp, port):
      self.s = socket.socket()
      self.localHost = serverIp
      self.port = port



   def startServer(self):
      self.s.bind((self.localHost, self.port))
      print('socket created')
      self.s.listen(2)
      print('waiting for connection')


   def dataProcess(self):
      while True:
         c, addr = self.s.accept()
         recived = c.recv(1024).decode()
         print('connect with', addr,recived)
         c.close()


if __name__ == '__main__':
   a = Server('localhost',9999,)
   a.startServer()
   a.dataProcess()
