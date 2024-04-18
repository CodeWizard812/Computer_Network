import socket

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def sendData(server_socket, data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)

    
    print("\nKey:", key)
    print("Original Data:", data)

    # Send CRC key and data to the server
    server_socket.send((key + ';' + data).encode())

# Set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

# Input the CRC key from the client
key = input("Enter the CRC Key: ")

# Input data to be sent
data = input("Enter the Data to be Sent: ")

# Send CRC key and data to the server
sendData(client_socket, data, key)

# Close the socket
client_socket.close()
