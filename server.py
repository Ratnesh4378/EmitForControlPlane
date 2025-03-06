import socket

def start_server(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind((ip, port))
    print(f"Server listening on {ip}:{port}")

    while True:
        packet, addr = sock.recvfrom(1024)  
        print(f"Received packet from {addr}: {packet.decode('utf-8')}")

if __name__ == "__main__":
    # server_ip = "10.129.2.173"  
    server_ip = "10.129.2.201"  
    server_port = 12345      

    start_server(server_ip, server_port)
