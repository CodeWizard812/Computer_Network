import socket

port=30000
portClient=4000
host="127.0.0.1"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.bind((host, portClient))
client.connect((host, port))

while True:	
	data = input("Enter your message: ")
	client.send(data.encode())

	if data=='bye':
		break

	recieved_data = client.recv(2048)
	print("Message from Server: ",recieved_data.decode())
		
print("Connection closed from server")
client.close()

