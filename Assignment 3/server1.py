import socket

port=30000
host="127.0.0.1"

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host, port))
print("socket binded to %s" %(port))

server.listen(2)
print("Socket is listening...")

# Accepting/Establishing connection from client.
conn, addr = server.accept()        
print('Got connection from', addr)

while True:
	recieved_data = conn.recv(2048)
	print("Message from client: ", recieved_data.decode())
	decoded_data = recieved_data.decode()

	if recieved_data.decode()=='bye':
		break
	
	characters = ""  # For storing Even or Odd characters

	for i in range(len(decoded_data)):
		if len(decoded_data) % 2 == 0:
			if i % 2 == 0:
				characters += decoded_data[i]
		elif i % 2 != 0 :
			characters += decoded_data[i]
		
	conn.send(characters.encode())

print("Connection closed from client")		

#Close the connection with the client
conn.close()

