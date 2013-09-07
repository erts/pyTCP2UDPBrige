import socket
import threading


MAX_LISTEN_COUNT = 1
MAX_DATA_LEN = 1024
DEFAULT_UDP_PORT = 5000

class TCP_UPD_Forwarder(threading.Thread):
    def __init__(self,port):
        threading.Thread.__init__(self)
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('',port))
        self.socket.listen(MAX_LISTEN_COUNT)


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

    def run(self):
        self.process_socket()
        

class UDP_TCP_Frowarder(threading.Thread):
    def __init__(self,remote_host,port):
        threading.Thread.__init__(self)
        if not port:
            port = DEFAULT_UDP_PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('',port))
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

    def run(self):
        self.process_socket()
        
        
def main():
    tcp_udp_forwarder = TCP_UPD_Forwarder(5000)
    tcp_udp_forwarder.start()
    tcp_udp_forwarder.join()
    udp_tcp_forwarder = UDP_TCP_Frowarder('127.0.0.1',9000)
    udp_tcp_forwarder.start()
    udp_tcp_forwarder.join()
        
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
    