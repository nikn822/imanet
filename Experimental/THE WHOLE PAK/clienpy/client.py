# Import socket module
import socket
import ast

from ast import literal_eval as make_tuple               
 
# Create a socket object
s = socket.socket()         
 
# Define the port on which you want to connect
port = 8080               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# receive data from the server
while True:
	jiff = ast.literal_eval(s.recv(1024))

	dog = dict(jiff)

	print dog['x']


# close the connection
