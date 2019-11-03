'''
Neil Shah
UCID: ns642
Section: 005
'''
import sys, time
from socket import*
import struct

argv = sys.argv
host = argv[1]
port = argv[2]

port = int(port)

totalPackets = 10
sentPackets = 0
recievedPackets = 0
lostPackets = 0
rtt = []

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

print("Pinging "+str(host)+str(port))

for i in range(10):
    sentPackets+=1
    msg = struct.pack('!II',1,i)
    startTime = time.time()
    clientSocket.sendto(msg, (host,port))
   
    try:
        dataEcho, address = clientSocket.recvfrom(len(msg))
        RTT = time.time()-startTime
        rtnMsg = struct.unpack('!II', dataEcho)
        if(RTT!=0): rtt.append(RTT)
        print("Ping message number "+str(i)+" RTT: "+str(RTT)+" secs")
        recievedPackets+=1
    except error:
        print("Ping message number "+str(i)+" timed out")
        lostPackets+=1

clientSocket.close();

packetLoss = (lostPackets/totalPackets)*100
maxRTT = max(rtt)
minRTT = min(rtt)
avgRTT = sum(rtt)/len(rtt)
print("\n---127.0.0.1 Ping Statistics---")
print("\n"+ str(sentPackets) + " packets sent, " + str(recievedPackets) + " packets recieved, "+str(packetLoss)+"% packet loss")
print("Min RTT: "+str(minRTT)+"  Avg RTT: "+str(avgRTT)+"  Max RTT: "+str(maxRTT))
