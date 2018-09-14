# first of all import the socket library

import socket 
import pandas as pd  
import time


df = pd.read_csv('data.csv')           
 
# next create a socket object
s = socket.socket()         
print "Socket successfully created"
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 8080               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests 
# coming from other computers on the network
s.bind(('', port))        
print "socket binded to %s" %(port)
 
# put the socket into listening mode
s.listen(5)     
print "socket is listening"           
 
# a forever loop until we interrupt it or 
# an error occurs
ct = 0
while True:
 
   # Establish connection with client.
   c, addr = s.accept()     
   print 'Got connection from', addr
   jiff = True
   while jiff == True:
	   nom = df.iloc[ct,1]
	   nomdeSt = str(nom)

	   mol = df.iloc[ct,0]
	   moldeSt = str(mol)

	   pop = df.iloc[ct,2]
	   popdeSt = str(pop)
	   
	   datadict = {'x':nom, 'y':mol, 'z':pop}

	   dataStr = str(datadict)
	   c.send(dataStr)
	   ct +=1
	   time.sleep(.1)
