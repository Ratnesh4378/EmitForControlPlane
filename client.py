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
    # client_ip = "10.129.2.173"  
    client_ip = "10.129.2.201"
    client_port = 12345      
    # data_to_send = "Hello, Client!"  

    while(1):
        bfrt.code4_2.pipe.IngressControl.c_tot_cnt.operation_counter_sync()
        cnt=bfrt.code4_2.pipe.IngressControl.c_tot_cnt.dump(return_ents=True)  
        data_to_send = cnt[0].data[b'$COUNTER_SPEC_PKTS']
        print(data_to_send)
        bfrt.code4_2.pipe.IngressControl.rclt_tot_cnt.get(0, from_hw=1)
        bfrt.code4_2.pipe.IngressControl.c_tot_cnt.get(0, from_hw=1)    
        send_packet_to_client(client_ip, client_port, data_to_send)
        time.sleep(5)
        
