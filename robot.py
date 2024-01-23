import l293d
import time
m1 = l293d.DC(22,18,16)
m2 = l293d.DC(15,13,11)
def forward(m1,m2):
    m1.clockwise(speed=100)
    m2.clockwise(speed=100)

def stop(m1,m2):
    #time.sleep(3)
    m1.stop()
    m2.stop()

def back(m1,m2):
    m1.anticlockwise(speed=100)
    m2.anticlockwise(speed=100)
    
def left(m1,m2):
    m1.clockwise(speed=100)
    
def right(m1,m2):    
    m2.clockwise(speed=100)
import socket
HOST = '0.0.0.0'
PORT = 50007
m1.clockwise(speed=100,duration=1)
m2.clockwise(speed=100,duration=1)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((HOST,PORT))
s.listen(1)
data,add = s.accept()
while True:    
    d,ip = data.recvfrom(1518)
    print(d)
    if d == b'end':
        break
    try:
        stop(m1,m2)
    except:
        pass
    if d == b"w":
        forward(m1,m2)
    elif d == b"s":
        back(m1,m2)
    elif d == b"d":
        left(m1,m2)
    elif d == b"a":
        right(m1,m2)
    elif d == b"z":
        stop(m1,m2)
        break
    else:
        stop(m1,m2)    
        
data.close()
l293d.cleanup()

