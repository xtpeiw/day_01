# udp_s.py

# import time
# time.asctime()

from socket import *

sockdf = socket(AF_INET,SOCK_DGRAM)


server_addr = ('0.0.0.0',13998)
sockdf.bind(server_addr)


while True:
    print('udb　服务器端')
    data,addr = sockdf.recvfrom(20)
    print('给你信息',(addr,data.decode()))

    sockdf.sendto('收到你的消息'.encode(),addr)

sockdf.close()