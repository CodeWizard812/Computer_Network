import socket

def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0: pick]
    
    print("\nDivisor:", divisor)
    print("Dividend:", dividend)

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    checkword = tmp
    return checkword

def receiveData(client_socket):
    # Receive data and CRC key from the client
    received_data = client_socket.recv(1024).decode()
    key, data = received_data.split(';')
    
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    checksum = mod2div(appended_data, key)

    print("\nKey:", key)
    print("Original Data:", data)
    print("Checksum:", checksum)
    print("Data Sent by Client:", data + checksum )
    print("Verification Result:", "Error Detected!" if checksum != '0'*(l_key-1) else "No Errors Detected")

# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

print("Server is listening for incoming connections...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print("Connection established with", client_address)

# Receive and process data from the client
receiveData(client_socket)

# Close the sockets
client_socket.close()
server_socket.close()
