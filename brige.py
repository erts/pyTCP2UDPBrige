import threading
import socket
import sys

LISTEN_TO_UDP_PORT = 5000

SEND_TO_UDP_IP = "127.0.0.1"
SEND_TO_UDP_PORT = 5000

TCP_SERVER_IP = "127.0.0.1"
TCP_SERVER_PORTS = [5000,5001,5002,]

        
class TCP_UDP_forwarder(threading.Thread):
    def __init__(self, tcp_server_ip, tcp_server_port):
        threading.Thread.__init__(self)
        self.tcp_server_ip = tcp_server_ip
        self.tcp_server_port = tcp_server_port
        self.tcp_server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_sock.bind((self.tcp_server_ip,self.tcp_server_port))
        self.tcp_server_sock.listen(5)
    def run(self):
        self.run_tcp_listener()
    
    def run_tcp_listener(self):
        while True:
            connection, client_address = self.tcp_server_sock.accept()
            try:
                print >>sys.stderr, 'connection from', client_address
                while True:
                    data = connection.recv(1024)
                    print >>sys.stderr, 'Address %s:%d received "%s"' % (self.tcp_server_ip, self.tcp_server_port, data)
                    if data:
                        self.send_data_over_udp_client(data)
                        print >>sys.stderr, 'sending data to the client'
                        connection.sendall(data)
                    else:
                        print >>sys.stderr, 'no more data from', client_address
                        break
            
            finally:
                connection.close()

    def send_data_over_udp_client(self,data):
        print "Send data to server over UDP, data: " + str(data)
        #client_udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #client_udp_socket.sendto(data,(SEND_TO_UDP_IP,SEND_TO_UDP_PORT))
        #for test! Should be removed in future
        #reveive_data, address = client_udp_socket.recvfrom(1024)
        #print str(reveive_data) + " from " +str(address)
        
def main():
    #manage list of forwarders
    tcp2udp_forwarders = []
    for port in TCP_SERVER_PORTS:
        print "Create address %s:%d ", TCP_SERVER_IP,port
        tcp2udp_forwarder = TCP_UDP_forwarder(TCP_SERVER_IP,port)
        tcp2udp_forwarders.append(tcp2udp_forwarder)
        tcp2udp_forwarder.start()

    for forward in tcp2udp_forwarders:
        forward.join()
        
    #manage listener and tcp clients
    
        
if "__main__" == __name__:
    main()
    
    