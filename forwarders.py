import socket

MAX_LISTEN_COUNT = 1
MAX_DATA_LEN = 1024
DEFAULT_UDP_PORT = 5000

class TCP_UPD_Forwarder():
    def __init__(self,port):
        self.port = port
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.bind('',port)
        socket.listen(MAX_LISTEN_COUNT)
        self.socket = socket

    def process_socket(self):
        while True:
            self.client_socket, self.client_address = self.socket.accept()
            while True:
                data = client_socket.recv(MAX_DATA_LEN)
                if data:
                    self.send_to_UDP(data)
                data = recv_from_UDP()
                if data:
                    client_socket.send(data)
        

    def send_to_UDP(self,data):
        #send data and self.port
        pass

    def recv_from_UDP(self):
        pass


class UDP_TCP_Frowarder():
    def __init__(self,remote_host,port):
        if not port:
            port = DEFAULT_UDP_PORT
        socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        scoket.bind('',port)
        self.socket = socket
        self.host = remote_host

    def process_socket(self):
        while True:
            data, address = self.socket.recvfrom(MAX_DATA_LEN)
            if data:
                send_to_TCP(data,address[1]) #address[1] is sender's port
            data, port = recv_from_TCP()
            if data:
               self.socket.sendto(data,(self.host,port))

    def recv_from_TCP(self):
        #recv data and port
        pass

    def send_to_TCP(self,data,port):
        #send data and port
        pass
