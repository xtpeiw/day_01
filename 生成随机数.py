#生成随机数.py
import random as r
import time

for q in range(60):

    # time.sleep(0.5)
    y = r.randrange(13)
    x = r.randrange(31)
    s = r.randrange(1,25)
    d = r.randrange(1,60)
    w = r.randrange(10000,10099)
    p = r.randrange(10000,10030)

    e=(('%02d,'%q)+'%d'%(w)+','+'%d'%(p)+','+"'2018-%02d-%02d %02d:%02d:%02d'"%(y,x,s,d,d))
    print('(%s)'%e,end=',')
    # print('%d,%s'%(qq,e))



