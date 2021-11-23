import socket
M_SIZE=1024
client_port=60000
server_port=60001
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server=socket.socket(socket.AF_INET,type=socket.SOCK_DGRAM)
server.bind(('127.0.0.1',server_port))

#send block --> input IP and message
#send_len=client.sendto(message.encode('utf-8'),(IP,client_port))

#recieve block
#rx_message,addr=server.recvfrom(M_SIZE)
