# coding: utf-8
import time

i=0
while(i<20):
    print('-----------main--------[',i,']')
    i+=1
    time.sleep(1)

print("ok man yeaaaahh!")

#rx_message,addr=server.recvfrom(M_SIZE)
#send_len=client.sendto(message.encode('utf-8'),('127.0.0.1',recieve_port))