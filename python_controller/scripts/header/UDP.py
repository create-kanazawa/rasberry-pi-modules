#-----------------------UDP header-----------------------
from __future__ import division
import socket
M_SIZE=1024
recieve_port=60000
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server=socket.socket(socket.AF_INET,type=socket.SOCK_DGRAM)
server.bind(('',recieve_port))
server.setblocking(False)
recieve_message = ''
#server.settimeout(0.1)


def recieve_data():
    global recieve_message
    print('wait for data...')
    while True:
        try:
            rx_message,addr=server.recvfrom(M_SIZE)
            recieve_message = rx_message.decode('utf-8')
        except:
            break
    return recieve_message

#send block --> input IP and message
#message='abcedf'
#IP='127.0.0.1'
#send_len=client.sendto(message.encode('utf-8'),(IP,recieve_port))

#recieve block
#rx_message,addr=server.recvfrom(M_SIZE)
#print(rx_message.decode('utf-8'))