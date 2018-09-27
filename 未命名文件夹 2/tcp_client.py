# // tcp_client.py
from socket import *
#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#发起连接
server_addr = ('0.0.0.0',26292)
sockfd.connect(server_addr)

while True:
    #消息发送接收
    data = input('请输入数据')
    sockfd.send(data.encode())
    if data == '':
        break
    data = sockfd.recv(1024)
    print('发送：',data.decode())

#关闭套接字
sockfd.close()
