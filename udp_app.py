import socket
import time

h_name = socket.gethostname()
IP_addres = socket.gethostbyname(h_name)

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(('0.0.0.0', 5353))

print(f"UDP server running on {IP_addres}:5353")

while True:
    msg, addr = udp_server.recvfrom(1024)
    current_time = time.strftime("%H:%M:%S")
    response = f"{current_time} Serving UDP from {h_name} ({IP_addres})\n"
    udp_server.sendto(response.encode(), addr)

