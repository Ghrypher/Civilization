import socket

class Network:
    def __init__(self):
        """Function __init__"""
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = '192.168.100.68'
        self.port = 5555
        self.address = self.server,self.port
        self.id = self.connect()
        print(self.id)

    def connect(self):
        """Function connect, is the conection trial"""
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            pass

net = Network()