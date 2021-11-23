# coding: utf-8
import time


print("start main")
i=0
while(1):
    print('-----------main aaaaa----------[',i,']')
    i+=1
    time.sleep(1)

f = open('sample.txt', 'w')
f.write('あははは\n')
f.close()

print("end main")
