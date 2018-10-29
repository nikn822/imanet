import socket 
import time
import random


port = 8080 
s = socket.socket() 
s.bind(('', port))   
print "socket binded to %s" %(port)
s.listen(5)     
print "socket is listening" 

c, addr = s.accept()  
print 'Got connection from', addr

lolVal = 78
while (lolVal>0):
	randInt = random.randint(1,101)

	print (randInt)

	stringNum = str(randInt)

	c.send(stringNum)

	