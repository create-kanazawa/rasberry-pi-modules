# coding: utf-8
import time

i=0
while(i<20):
    print('-----------main--------[',i,']')
    i+=1
    time.sleep(1)

print("ok man yeaaahh!")

#send block --> input IP and message
#message='abcedf'
#IP='127.0.0.1'
#send_len=client.sendto(message.encode('utf-8'),(IP,recieve_port))

#recieve block -->None
#rx_message,addr=server.recvfrom(M_SIZE)
#print(rx_message.decode('utf-8'))
