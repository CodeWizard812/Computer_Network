import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((SERVER_IP, SERVER_PORT))

server_socket.listen(5)
print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

arp_table = {}

def handle_arp_request(ip_address):
    if ip_address in arp_table:
        return arp_table[ip_address]
    else:
        return "IP address not found in ARP table"


def handle_client_connection(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        if data.startswith("ARP_REQUEST"):
            ip_address = data.split()[1]
            mac_address = handle_arp_request(ip_address)
            response = f"ARP_RESPONSE {mac_address}"
            client_socket.send(response.encode())

    client_socket.close()

while True:
    
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address[0]}:{client_address[1]}")

    client_handler = threading.Thread(target=handle_client_connection, args=(client_socket,))
    client_handler.start()