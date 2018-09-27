# b_send.py
#广播
from socket import *
from time import sleep


dest = ('0.0.0.0',55483)
s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

while True:
    sleep(0.8)
    s.sendto('go 天王盖地虎'.encode(),dest)

s.close()