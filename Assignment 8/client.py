import socket

def start_client():
    host = "127.0.0.1"
    port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter message to send (type 'quit' to close connection): ")
        if message == "quit":
            break
        client_socket.send(message.encode("utf-8"))
        response = client_socket.recv(1024)
        print(f"Server response: {response.decode('utf-8')}")
        server_message = client_socket.recv(1024)
        print(f"Server message: {server_message.decode('utf-8')}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
