import socket
import time

def create_packet(data):
    packet = f"Packet Data: {data}".encode('utf-8')
    return packet

def send_packet_to_client(ip, port, data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    packet = create_packet(data)
    
    try:
        sock.sendto(packet, (ip, port))
        print(f"Packet sent to {ip}:{port}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    client_ip = "10.129.2.173"  
    client_port = 12345      
    data_to_send = "Hello, Client!"  

    while(1):
        send_packet_to_client(client_ip, client_port, data_to_send)
        time.sleep(5)
        
