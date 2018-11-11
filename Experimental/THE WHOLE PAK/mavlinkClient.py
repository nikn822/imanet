from __future__ import print_function

import time

from pymavlink import mavutil

from tkinter import *


def GuiStartCMD():


	master = Tk()

	labl = Label(master, text = "Enter IP Address of server followed by port in the format: 000.000.000.000:0000 and then close window")
	labl.pack()

	e = Entry(master)
	e.pack()

	e.focus_set()

	ipAddr = ''

	def callback():
		master.quit()

	b = Button(master, text="Change IP", width=10, command =callback)
	b.pack()

	mainloop()

	text = e.get()
	newIP = str(text)
	print ("ipaddr: ",newIP)
	return text

startGui = GuiStartCMD()
newdevice = mavutil.mavlink_connection(('tcp:'+startGui), planner_format=True, notimestamps=False, robust_parsing=True) 

<<<<<<< HEAD
source = ColumnDataSource(dict(s=[], r=[]))
r = Figure(width=1000, height=300, title='Random Number Recieved')
r.line(source=source, x='s', y='r', line_width=2, alpha= .85, color= 'purple')

def update_data():
		global ct, data
		ct += 1


	while (lolWhile >0):
		time.sleep(0.0100)
		data = int (newdevice.recv())
		print(data)

		
	new_data = dict(s=[ct],y=[data])
	source.stream(new_data,100)



=======
lolWhile = 9
>>>>>>> parent of d69327d... Live Plotting

while (lolWhile >0):
	  time.sleep(0.0100)
	  data = str (newdevice.recv())
	  print(data)


