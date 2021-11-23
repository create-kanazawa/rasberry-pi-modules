import socket
M_SIZE=1024
recieve_port=60000
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server=socket.socket(socket.AF_INET,type=socket.SOCK_DGRAM)
server.bind(('',recieve_port))

#send block --> input IP and message
#send_len=client.sendto(message.encode('utf-8'),(IP,recieve_port))

#recieve block
#rx_message,addr=server.recvfrom(M_SIZE)

#get message string
#rx_message.decode('utf-8')