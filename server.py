'''
Name: Neil Shah
UCID: ns642
Section: 005
'''
import sys, time
from socket import*
import struct
import random

host = "localhost"
port = 8000
length = 10000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((host, port))

print('The server is ready to recieve on port: '+str(port))

while True:
    randNum = random.randint(0,10)
    
    data,address = serverSocket.recvfrom(length)
    
    
    msg = struct.unpack('!II', data)

    time.sleep(0.5)

    if(randNum<4):
        print("Message with sequence number "+str(msg[1])+" dropped")
    else:
        print("Responding to ping request with sequence number "+str(msg[1]))
        rtnMsg = struct.pack('!II', 2, msg[1])
        serverSocket.sendto(rtnMsg, address)
