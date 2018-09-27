#!/usr/bin/env/ python3
# import sys


# wo = sys.argv[0]
# # im = sys.argv[1]
# print(wo)
# print('-------------------')
# print(sys.argv[1])

# from socket import *
# s = socket()

# s.setsockopt(SOL_SOCKET,SO_REUSEADDR,10)


# print(s.setsockopt(SOL_SOCKET,SO_REUSEADDR))
# # #获取套接字的地址族类型
# print(s.family)
# print(s.type)
# s.bind(('0.0.0.0',13211))
# print(s.getsockname())
# print(s.fileno())
# s.listen(1)
# while True:
#     c,addr = s.accept()
#     print('地址',c.getpeername())
#     c.recv(1234)
# # telnet 地址　端口


#广播
# from socket import *

# s = socket(AF_INET,SOCK_DGRAM)

# #设置套接字可以发送接收广播
# s.setsockopt(SOL_SOCKET,SO_BROADCAST,5)

# #固定接收端口
# s.bind(('0.0.0.0',55483))

# while True:
#     try:
#         msg,addr = s.recvfrom(528)
#         print('从{}获取信息：{}').\
#                 format(addr,msg.decode())
#     except (KeyboardInterrupt,SyntaxError):
#         reise
#     except Exception as cc:
#         print(cc)
# s.close()

#http
from socket import *

#创建tcp套接字
s = socket()

s.bind(('0.0.0.0',4321))
s.listen(5)

while True:
    c,addr = s.accept()
    print('你接收到的',addr)

    data = c.recv(4086)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(data)  #浏览器发来的http请求
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    data= '''HTTP/1.1 200 OK 
        　
         Content-Encoding: gzip
         Content-Type: text/html

         <h1>哈哈</h1>
         '''
    c.send(data.encode())
    c.close()

s.close()














