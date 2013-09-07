import threading
import socket


LISTEN_TO_UDP_PORT = 5000

SEND_TO_UDP_IP = "127.0.0.1"
SEND_TO_UDP_PORT = 5000

TCP_SERVER_IP = "127.0.0.1"
TCP_SERVER_PORTS = [5000,5002,5003]

        
class TCP_UDP_forwarder(threading.Thread):
    def __init__(self, tcp_server_ip, tcp_server_port):
        threading.Thread.__init_(self)
        self.tcp_server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_sock.bind((tcp_server_id, tcp_server_port))
        
    def run(self):
        self.run_tcp_listener()
    
    def run_tcp_listener(self):
        self.tcp_server_sock.listen(1)
        conn, addr = self.tcp_server_sock.accept()
        while 1:
            data = conn.recv(1024)
            if not data:
                print "No data received!"
                break
            print "Received data from TCP socket: " + str(data)
            self.send_data_over_udp_client(data)
            conn.close()
            
    def send_data_over_udp_client(self,data):
        client_udp_socket = socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_udp_socket.sendto(data,(SEND_TO_UDP_IP,SEND_TO_UDP_PORT))
        
        #for test! Should be removed in future
        reveive_data, address = client_udp_socket.recvfrom(1024)
        print str(reveive_data) + " from " +str(address)
        
def main():
    #manage list of forwarders
    tcp2udp_forwarders = []
    for port in TCP_SERVER_PORTS:
        tcp2udp_forwarder = TCP_UDP_forwarder(TCP_SERVER_IP,port)
        tcp2udp_forwarders.append(tcp2udp_forwarder)
        tcp2udp_forwarder.start()
        tcp2udp_forwarder.join()
        
    #manage listener and tcp clients
    
        
if "__main__" == __name__:
    main()
    
    