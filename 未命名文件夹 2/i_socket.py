# import socket


# sockfd = socket.socket(socket_family = AF_INET,
#                         socket_type = SOCK_STREAM,
#                         proto = 0)

# sockfd.bind(addr) 



from socket import *

#创建套接字
sockfd = socket(AF_INET,SOCK_STREAM)


#帮定IP地址
sockfd.bind(('0.0.0.0',33665))

#设置监听
sockfd.listen(5)

#等待接受连接
print('服务器端')
connfd,addr = sockfd.accept()
print('主机地址',addr)

while True:
    #收发信息
    data = connfd.recv(1024).decode()
    if data == 'bb':
        break
    print(data)
    n = connfd.send(b'Receine your message')
    print('接收到了%d字节'%n)

#关闭套接字
connfd.close()
sockfd.close()

