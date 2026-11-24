import socket
from pathlib import Path

data = Path(__file__).with_name("message.json").read_bytes()
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    #sock.sendto(data, ("192.168.0.255", 5000))
    sock.sendto(data, ("192.168.0.101", 5001))
    
print("已发送 message.json")
