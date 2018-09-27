# udb_c.py
from socket import *
import sys



if len(sys.argv)< 3:
    print('地址不对')
    raise

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

soso = socket(AF_INET,SOCK_DGRAM)

while True:
    data = input('消息')
    if not data:
        break
    soso.sendto(data.encode(),ADDR)
    data,addr = soso.recvfrom(500)
    print('从服务器收到',data.decode())

soso.close()


