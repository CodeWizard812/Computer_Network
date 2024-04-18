import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode("utf-8")
        print(f"Received message from {client_address}: {message}")
        response = f"You sent: {message}"
        client_socket.send(response.encode("utf-8"))
        server_input = input(f"Enter message to client {client_address}: ")
        client_socket.send(server_input.encode("utf-8"))

    print(f"Connection from {client_address} closed")
    client_socket.close()

def start_server():
    host = "127.0.0.1"
    port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
