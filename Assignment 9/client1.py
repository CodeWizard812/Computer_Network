import socket

def main():
    server_host = "127.0.0.1"
    server_port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))

    while True:
        ip_address = input("Enter IP address (type 'exit' to quit): ")
        if ip_address.lower() == 'exit':
            break
        client_socket.send(ip_address.encode())
        mac_address = client_socket.recv(1024).decode()
        print(f"The MAC address corresponding to {ip_address} is {mac_address}")

    client_socket.close()

if __name__ == "__main__":
    main()
