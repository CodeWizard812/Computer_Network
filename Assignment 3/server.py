import socket
port = 50000
host = "127.0.0.1"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host,port))
print("Server Binded to %s" %(port))

server.listen(2)
print("Server is Listening...")

def postfix(exp):
    stack = []
    operator = set(['+', '-', '/', '*'])

    for char in exp:
        if char.isdigit():
            stack.append(int(char))
        elif char in operator:
            op2 = stack.pop()
            op1 = stack.pop()

            if char == '+':
                res = op2 + op1
            if char == '-':
                res = op1 - op2
            if char == '*':
                res = op2 * op1
            if char == '/':
                res = op1 + op2

            stack.append(res)
    
    return stack[0]


conn, addr = server.accept()
print('G c f', addr)
while True:
    data = conn.recv(2048)
    print("Message from client: ", data.decode()) 
    if data.decode()=='quit':
        break
    ans = postfix(data.decode())
    print(ans)
print("Connection closed from client")        

#Close the connection with the client
conn.close()